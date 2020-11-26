<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-cascades"></i> 接口用例管理</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
        <div class="handle-box">
                <el-button type="primary"  class="handle-del mr10" @click="add">新增数据</el-button>
                <el-button type="primary"  class="handle-del mr10" @click="handlebatchRun">批量运行</el-button>
          </div>
           <div class="handle-box">
                <el-button type="primary" icon="delete" class="handle-del mr10" @click="delAll">批量删除</el-button>
                <el-select v-model="select_cate" placeholder="筛选项目" class="handle-select mr10">
                    <el-option key="1" label="修连邦" value="修连邦"></el-option>
                    <el-option key="2" label="车有料" value="车有料"></el-option>
                </el-select>
                <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="search" @click="search">搜索</el-button>
            </div>
            <el-table :data="tableData" border class="table" ref="multipleTable" @selection-change="handleSelectionChange">
               <el-table-column type="selection" width="55" align="center"></el-table-column>

                <el-table-column prop="case_id" label="id" width='80'>
                </el-table-column>
                <el-table-column prop="project" label="测试项目" width='150' >
                </el-table-column>
                <el-table-column prop="title" label="测试标题"  width='180'>
                </el-table-column>
                <el-table-column prop="is_run" label="是否运行" width="120">
                <template slot-scope="scope">
                    <el-switch
                    v-model="scope.row.is_run"
                    :active-value = "1"
                    :inactive-value = "0"
                    @change="changeSwicth($event,scope.row)"
                    ></el-switch>
                </template>
                </el-table-column>
                
                <el-table-column prop="result" label="测试结果"  width='180'>
                    <template slot-scope="scope">
                        <el-label>{{scope.row.result === 0? "停止执行" :scope.row.result == 1 ?"通过" : "失败"}}</el-label>
                    </template>
                </el-table-column>                                


                <el-table-column label="操作" width="180" align="center">
                    <template slot-scope="scope">
                        <el-button type="text" icon="el-icon-edit" @click="goStepList( scope.row)">查看</el-button>
                        <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>



           <!-- 下面的分页展示total="1000"这是总共多少条数据-->
            <div class="pagination">
                <el-pagination background @current-change="handleCurrentChange" layout="prev, pager, next" :total="1000">
                </el-pagination>
            </div>

        </div>

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" :visible.sync="editVisible" width="30%">    
            <el-form ref="form" :model="form" label-width="120px">
                <!--
                <el-form-item label="用例id">
                    <el-input v-model="form.case_id"  placeholder="id为空就是新增数据" ></el-input>
                </el-form-item>
                -->
                <el-form-item label="测试项目">
                    <el-input v-model="form.project"></el-input>
                </el-form-item>
                <el-form-item label="测试标题">
                    <el-input v-model="form.title"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="editVisible = false">取 消</el-button>
                <el-button type="primary" @click="saveEdit">确 定</el-button>
            </span>
        </el-dialog>

        <!-- 删除提示框 -->
        <el-dialog title="提示" :visible.sync="delVisible" width="300px" center>
            <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="delVisible = false">取 消</el-button>
                <el-button type="primary" @click="deleteRow">确 定</el-button>
            </span>
        </el-dialog>

        <!-- 批量运行提示框 -->
        <el-dialog title="提示" :visible.sync="batchRunVisible" width="300px" center>
            <div class="del-dialog-cnt">是否确定批量运行？</div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="batchRunVisible = false">取 消</el-button>
                <el-button type="primary" @click="definiteRun">确 定</el-button>
            </span>
        </el-dialog>    
    </div>
</template>

<script>
    export default {
        name: 'basetable',
        data() {
            return {
                url: './static/vuetable.json',
                tableData: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                del_list: [],
                is_search: false,
                editVisible: false,
                delVisible: false,
                batchRunVisible: false,
                form: {
                    name: '',
                    date: '',
                    address: ''
                },
                idx: -1,
                deleteid:''
            }
        },
        created() {
            this.getData();
        },
        computed: {
            data() {
                return this.tableData.filter((d) => {
                    let is_del = false;
                    for (let i = 0; i < this.del_list.length; i++) {
                        if (d.name === this.del_list[i].name) {
                            is_del = true;
                            break;
                        }
                    }
                })
            }
        },
        methods: {
            // 分页导航
            handleCurrentChange(val) {
                this.cur_page = val;
                this.getData();
            },

            //获取数据
             getData() {
                this.url = 'apicase/caselist';
                this.$axios(this.url).then((res) => {
                    console.log("接口用例api返回数据",res.data.data)
                    this.tableData = res.data.data.rows;
                })
            },
            add(){
              console.log("点击新增")
              this.form = {}
              this.editVisible = true;

            },
            search() {
                this.$message.error('功能暂未完善');
                this.is_search = true;
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            //批量运行
            handlebatchRun(){
                console.log("点击批量运行")
                this.batchRunVisible = true;
            },
            //更改运行状态
            changeSwicth(Swicthdata,row){
                console.log("切换状态",Swicthdata,row)
                this.url = '/apicase/caselist/updaterun' 
                let data={"id":row.id,
                        "is_run":Swicthdata}

                this.$axios.post(this.url,data).then((res) => {
                    console.log("切换状态返回数据",res.data.message)
                this.$message.success('切换状态成功');
                })                       
                

            },            
            handleEdit(index, row) {
                console.log("点击编辑")
                this.idx = index;
                const item = this.tableData[index];
                this.form = item
                this.editVisible = true;
            },
            handleDelete(index, row) {
                console.log("点击删除按钮",index,"删除id",row.id)
                this.idx = index;
                this.deleteid=row.id;
                this.delVisible = true;
            },
            delAll() {
                const length = this.multipleSelection.length;
                let str = '';
                this.del_list = this.del_list.concat(this.multipleSelection);
                for (let i = 0; i < length; i++) {
                    str += this.multipleSelection[i].name + ' ';
                }
                this.$message.error('删除了' + str);
                this.multipleSelection = [];
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            // 保存编辑
            saveEdit() {
                this.$set(this.tableData, this.idx, this.form);
                console.log("提交修改信息",this.form)
                this.editVisible = false;
                this.$message.success(`操作成功`);
                // this.$axios.post('api',this.form).then((res) => {
                //     console.log("修改信息返回数据",res)
                //      this.getData();
                // })
            },
            // 确定删除
            deleteRow(){
                this.tableData.splice(this.idx, 1);
                console.log("删除提交数据id",this.deleteid)
                this.$message.success('删除成功');
                this.delVisible = false;

                //  this.url = 'apicase/caselist';
                // this.$axios(this.url).then((res) => {
                //     console.log("接口用例api返回数据",res.data.data)
                //     this.tableData = res.data.data.rows;
                // })


                this.$axios.post('/apicase/caselist/delectcase',{case_id:this.deleteid}).then((res) => {
                    console.log("删除信息返回数据",res)
                })
            },
            goStepList(row){
                console.log("跳转测试",row.case_id)
                //let jumpid=e.case_id
                let data = {"case_id":row.case_id} 
                console.log("data",data)
                
                //this.$router.push({path:'/CaseStepManage',params:data})
                this.$router.push({name:'CaseStepManage',query:data})

            },
            definiteRun(){
                this.url = 'apicase/run';
                let data={"case_id":"all"}

                this.$axios.post(this.url,data).then((res) => {
                    console.log("批量运行返回数据",res.data.data)
                this.$message.success('运行成功');
                this.batchRunVisible = false;
                })                
            }
        }
    }

</script>

<style scoped>
    .handle-box {
        margin-bottom: 20px;
    }

    .handle-select {
        width: 120px;
    }

    .handle-input {
        width: 300px;
        display: inline-block;
    }
    .del-dialog-cnt{
        font-size: 16px;
        text-align: center
    }
    .table{
        width: 100%;
        font-size: 14px;
    }
    .red{
        color: #ff0000;
    }
</style>
