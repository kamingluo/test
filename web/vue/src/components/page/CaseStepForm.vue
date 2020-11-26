<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-calendar"></i> 测试步骤表单</el-breadcrumb-item>
                <el-breadcrumb-item></el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <!--冒号表示动态绑定!-->
                <el-form ref="form" :model="form" :rules="rules" label-width="80px">
                    <el-form-item label="步骤ID" prop="step_id">
                        <el-input v-model="form.step_id"></el-input>
                    </el-form-item>                    
                    <el-form-item label="步骤名称" prop="step_title">
                        <el-input v-model="form.step_title" ></el-input>
                    </el-form-item>
                    <el-form-item label="接口地址" prop="url">
                        <el-input v-model="form.url"></el-input>
                    </el-form-item>
                    <el-form-item label="测试方法" prop="method">
                        <el-input v-model="form.method"></el-input>
                    </el-form-item>
                    <el-form-item label="header前置步骤">
                        <el-input v-model="form.prepose_header_step"></el-input>
                    </el-form-item>              
                    <el-form-item label="header依赖字段">
                        <el-input v-model="form.prepose_header_key"></el-input>
                    </el-form-item>
                    <el-form-item label="header" prop="header">
                        <el-input type="textarea" rows="5" v-model="form.header"></el-input>
                    </el-form-item>                                    
                    <el-form-item label="body前置步骤">
                        <el-input v-model="form.prepose_body_step"></el-input>
                    </el-form-item>              
                    <el-form-item label="body依赖字段">
                        <el-input v-model="form.prepose_body_key"></el-input>
                    </el-form-item>
                    <el-form-item label="请求体" prop="body">
                        <el-input type="textarea" rows="5" v-model="form.body"></el-input>
                    </el-form-item>  

                    <el-form-item label="断言等级" prop="assert_level">
                        <el-select v-model="form.assert_level" placeholder="请选择">
                            <el-option key="0" label="0" value=0></el-option>
                            <el-option key="1" label="1" value=1></el-option>
                            <el-option key="2" label="2" value=2></el-option>
                        </el-select>
                    </el-form-item>                    
                    <el-form-item label="运行开关">
                        <el-switch v-model="form.is_run"
                        :active-value = "1"
                        :inactive-value = "0"
                        ></el-switch>                   
                    </el-form-item>
                    <el-form-item label="预期code值">
                        <el-input type="textarea" rows="1" v-model="form.expect_code"></el-input>
                    </el-form-item>
                    <el-form-item label="预期结果">
                        <el-input type="textarea" rows="5" v-model="form.expect_result"></el-input>
                    </el-form-item>                    
                    
                    <el-form-item>
                        <el-button>取消</el-button>
                        <el-button type="primary" @click="onSubmit('form')">表单提交</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: 'baseform',
        data: function(){
            return {
                form: {
                        case_id:'',
                        step_id:'',
                        is_run:'',
                        step_title:'',
                        url:'',
                        method:'',
                        prepose_header_step:'',
                        prepose_header_key:'',
                        header:'',
                        prepose_body_step:'',
                        prepose_body_key:'',
                        body:'',
                        return_key:'',
                        return_value:'',
                        assert_level:'',
                        expect_code:'',
                        expect_result:'',
                        result:''
                },
                form2:{
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: true,
                    type: ['步步高'],
                    resource: '小天才',
                    desc: ''
                },
                // 校验规则
                rules:{
                    step_id:[{
                        required: true,
                        message: '请填写步骤ID', //规则提示
                        trigger: 'blur'
                    
                    }],
                    step_title:[{
                        required: true,
                        message: '请填写步骤名称', //规则提示
                        trigger: 'blur'   

                    }],
                    url:[{
                        required: true,
                        message: '请填写接口地址', //规则提示
                        trigger: 'blur'   

                    }],
                    method:[{
                        required: true,
                        message: '请填写测试方法', //规则提示
                        trigger: 'blur'   

                    }],                    
                    assert_level:[{
                        required: true,
                        message: '请填写断言等级', //规则提示
                        trigger: 'blur'   

                    }]
                }
            }
        },
        activated(){
            console.log("刷新页面")
            //
            console.log("路由传输参数",this.$route.params)
            if (this.$route.params.step_id){
                console.log("状态为编辑")
                this.url = '/apicase/steplist/update' 
                this.form = this.$route.params
            }
            
            else{
                console.log("状态为新增")
                this.url = '/apicase/steplist/add' 
                this.form.case_id  = this.$route.params.case_id
                  
            }
            console.log("步骤信息",this.form)

        },
        methods: {
            onSubmit(formdata) {
                this.$refs[formdata].validate(valid => {
                    if  (valid){
                        let data= this.form       

                        this.$axios.post(this.url,data).then((res) => {
                            this.$message.success('提交成功！');
                            })
                        this.$router.go(-1)
                        this.$store.dispatch('delVisitedViews', this.$route);    
                    }else{
                        console.log('error submit!!')
                    }
            
            
                })
            }
        }
    }
</script>