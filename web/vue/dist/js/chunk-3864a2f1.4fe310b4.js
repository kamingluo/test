(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3864a2f1"],{"0a49":function(t,e,s){var n=s("9b43"),i=s("626a"),a=s("4bf8"),l=s("9def"),o=s("cd1c");t.exports=function(t,e){var s=1==t,c=2==t,r=3==t,u=4==t,d=6==t,f=5==t||d,h=e||o;return function(e,o,m){for(var p,v,g=a(e),_=i(g),b=n(o,m,3),x=l(_.length),C=0,w=s?h(e,x):c?h(e,0):void 0;x>C;C++)if((f||C in _)&&(p=_[C],v=b(p,C,g),t))if(s)w[C]=v;else if(v)switch(t){case 3:return!0;case 5:return p;case 6:return C;case 2:w.push(p)}else if(u)return!1;return d?-1:r||u?u:w}}},1169:function(t,e,s){var n=s("2d95");t.exports=Array.isArray||function(t){return"Array"==n(t)}},1754:function(t,e,s){"use strict";var n=s("6121"),i=s.n(n);i.a},"214f":function(t,e,s){"use strict";var n=s("32e9"),i=s("2aba"),a=s("79e5"),l=s("be13"),o=s("2b4c");t.exports=function(t,e,s){var c=o(t),r=s(l,c,""[t]),u=r[0],d=r[1];a(function(){var e={};return e[c]=function(){return 7},7!=""[t](e)})&&(i(String.prototype,t,u),n(RegExp.prototype,c,2==e?function(t,e){return d.call(t,this,e)}:function(t){return d.call(t,this)}))}},"5ebe":function(t,e,s){},6121:function(t,e,s){},"727c":function(t,e,s){"use strict";var n=s("da8f"),i=s.n(n);i.a},"759f":function(t,e,s){"use strict";var n=s("5ca1"),i=s("0a49")(3);n(n.P+n.F*!s("2f21")([].some,!0),"Array",{some:function(t){return i(this,t,arguments[1])}})},"7f7f":function(t,e,s){var n=s("86cc").f,i=Function.prototype,a=/^\s*function ([^ (]*)/,l="name";l in i||s("9e1e")&&n(i,l,{configurable:!0,get:function(){try{return(""+this).match(a)[1]}catch(t){return""}}})},a481:function(t,e,s){s("214f")("replace",2,function(t,e,s){return[function(n,i){"use strict";var a=t(this),l=void 0==n?void 0:n[e];return void 0!==l?l.call(n,a,i):s.call(String(a),n,i)},s]})},bfe9:function(t,e,s){"use strict";s.r(e);var n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"wrapper"},[s("v-head"),s("v-sidebar"),s("div",{staticClass:"content-box",class:{"content-collapse":t.collapse}},[s("v-tags"),s("div",{staticClass:"content"},[s("transition",{attrs:{name:"move",mode:"out-in"}},[s("keep-alive",{attrs:{include:t.tagsList}},[s("router-view")],1)],1)],1)],1)],1)},i=[],a=(s("7f7f"),function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"header"},[s("div",{staticClass:"collapse-btn",on:{click:t.collapseChage}},[s("i",{staticClass:"el-icon-menu"})]),s("div",{staticClass:"logo"},[t._v("测试后台管理系统")]),s("div",{staticClass:"header-right"},[s("div",{staticClass:"header-user-con"},[s("div",{staticClass:"btn-fullscreen",on:{click:t.handleFullScreen}},[s("el-tooltip",{attrs:{effect:"dark",content:t.fullscreen?"取消全屏":"全屏",placement:"bottom"}},[s("i",{staticClass:"el-icon-rank"})])],1),t._m(0),s("el-dropdown",{staticClass:"user-name",attrs:{trigger:"click"},on:{command:t.handleCommand}},[s("span",{staticClass:"el-dropdown-link"},[t._v("\n                    "+t._s(t.username)+" "),s("i",{staticClass:"el-icon-caret-bottom"})]),s("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[s("el-dropdown-item",{attrs:{divided:"",command:"loginout"}},[t._v("退出登录")])],1)],1)],1)])])}),l=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"user-avator"},[n("img",{attrs:{src:s("da26")}})])}],o=s("a026"),c=new o["default"],r=c,u={data:function(){return{collapse:!1,fullscreen:!1,name:"linxin",message:2}},computed:{username:function(){var t=localStorage.getItem("ms_username");return t||this.name}},methods:{handleCommand:function(t){"loginout"==t&&(localStorage.removeItem("ms_username"),this.$router.push("/login"))},collapseChage:function(){this.collapse=!this.collapse,r.$emit("collapse",this.collapse)},handleFullScreen:function(){var t=document.documentElement;this.fullscreen?document.exitFullscreen?document.exitFullscreen():document.webkitCancelFullScreen?document.webkitCancelFullScreen():document.mozCancelFullScreen?document.mozCancelFullScreen():document.msExitFullscreen&&document.msExitFullscreen():t.requestFullscreen?t.requestFullscreen():t.webkitRequestFullScreen?t.webkitRequestFullScreen():t.mozRequestFullScreen?t.mozRequestFullScreen():t.msRequestFullscreen&&t.msRequestFullscreen(),this.fullscreen=!this.fullscreen}},mounted:function(){document.body.clientWidth<1500&&this.collapseChage()}},d=u,f=(s("727c"),s("2877")),h=Object(f["a"])(d,a,l,!1,null,"e9e787d8",null);h.options.__file="Header.vue";var m=h.exports,p=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"sidebar"},[s("el-menu",{staticClass:"sidebar-el-menu",attrs:{"default-active":t.onRoutes,collapse:t.collapse,"background-color":"#324157","text-color":"#bfcbd9","active-text-color":"#20a0ff","unique-opened":"",router:""}},[t._l(t.items,function(e){return[e.subs?[s("el-submenu",{key:e.index,attrs:{index:e.index}},[s("template",{slot:"title"},[s("i",{class:e.icon}),s("span",{attrs:{slot:"title"},slot:"title"},[t._v(t._s(e.title))])]),t._l(e.subs,function(e){return[e.subs?s("el-submenu",{key:e.index,attrs:{index:e.index}},[s("template",{slot:"title"},[t._v(t._s(e.title))]),t._l(e.subs,function(e,n){return s("el-menu-item",{key:n,attrs:{index:e.index}},[t._v("\n                                "+t._s(e.title)+"\n                            ")])})],2):s("el-menu-item",{key:e.index,attrs:{index:e.index}},[t._v("\n                            "+t._s(e.title)+"\n                        ")])]})],2)]:[s("el-menu-item",{key:e.index,attrs:{index:e.index}},[s("i",{class:e.icon}),s("span",{attrs:{slot:"title"},slot:"title"},[t._v(t._s(e.title))])])]]})],2)],1)},v=[],g=(s("a481"),{data:function(){return{collapse:!1,items:[{icon:"el-icon-lx-home",index:"dashboard",title:"系统首页"},{icon:"el-icon-lx-cascades",index:"runapi",title:"接口测试"},{icon:"el-icon-lx-cascades",index:"ApiCaseManage",title:"接口用例管理"}]}},computed:{onRoutes:function(){return this.$route.path.replace("/","")}},created:function(){var t=this;r.$on("collapse",function(e){t.collapse=e})}}),_=g,b=(s("1754"),Object(f["a"])(_,p,v,!1,null,"7d1cf1f2",null));b.options.__file="Sidebar.vue";var x=b.exports,C=function(){var t=this,e=t.$createElement,s=t._self._c||e;return t.showTags?s("div",{staticClass:"tags"},[s("ul",t._l(t.tagsList,function(e,n){return s("li",{key:n,staticClass:"tags-li",class:{active:t.isActive(e.path)}},[s("router-link",{staticClass:"tags-li-title",attrs:{to:e.path}},[t._v("\n                "+t._s(e.title)+"\n            ")]),s("span",{staticClass:"tags-li-icon",on:{click:function(e){t.closeTags(n)}}},[s("i",{staticClass:"el-icon-close"})])],1)})),s("div",{staticClass:"tags-close-box"},[s("el-dropdown",{on:{command:t.handleTags}},[s("el-button",{attrs:{size:"mini",type:"primary"}},[t._v("\n                标签选项"),s("i",{staticClass:"el-icon-arrow-down el-icon--right"})]),s("el-dropdown-menu",{attrs:{slot:"dropdown",size:"small"},slot:"dropdown"},[s("el-dropdown-item",{attrs:{command:"other"}},[t._v("关闭其他")]),s("el-dropdown-item",{attrs:{command:"all"}},[t._v("关闭所有")])],1)],1)],1)]):t._e()},w=[],L=(s("759f"),s("d25f"),{data:function(){return{tagsList:[]}},methods:{isActive:function(t){return t===this.$route.fullPath},closeTags:function(t){var e=this.tagsList.splice(t,1)[0],s=this.tagsList[t]?this.tagsList[t]:this.tagsList[t-1];s?e.path===this.$route.fullPath&&this.$router.push(s.path):this.$router.push("/")},closeAll:function(){this.tagsList=[],this.$router.push("/")},closeOther:function(){var t=this,e=this.tagsList.filter(function(e){return e.path===t.$route.fullPath});this.tagsList=e},setTags:function(t){console.log("拿到的新增标题名字",t.meta.title);var e=this.tagsList.some(function(e){return e.path===t.fullPath});if(!e){this.tagsList.length>=8&&this.tagsList.shift();for(var s=0;s<this.tagsList.length;s++)console.log("tagsList",this.tagsList[s]),t.meta.title==this.tagsList[s].title&&(console.log("有相同的啊"),this.tagsList.splice(s),console.log("删除后的数组",this.tagsList));this.tagsList.push({title:t.meta.title,path:t.fullPath,name:t.matched[1].components.default.name})}r.$emit("tags",this.tagsList)},handleTags:function(t){"other"===t?this.closeOther():this.closeAll()}},computed:{showTags:function(){return this.tagsList.length>0}},watch:{$route:function(t,e){this.setTags(t)}},created:function(){this.setTags(this.$route)}}),k=L,y=(s("c5f3"),Object(f["a"])(k,C,w,!1,null,null,null));y.options.__file="Tags.vue";var F=y.exports,$={data:function(){return{tagsList:[],collapse:!1}},components:{vHead:m,vSidebar:x,vTags:F},created:function(){var t=this;r.$on("collapse",function(e){t.collapse=e}),r.$on("tags",function(e){for(var s=[],n=0,i=e.length;n<i;n++)e[n].name&&s.push(e[n].name);t.tagsList=s})}},S=$,A=Object(f["a"])(S,n,i,!1,null,null,null);A.options.__file="Home.vue";e["default"]=A.exports},c5f3:function(t,e,s){"use strict";var n=s("5ebe"),i=s.n(n);i.a},cd1c:function(t,e,s){var n=s("e853");t.exports=function(t,e){return new(n(t))(e)}},d25f:function(t,e,s){"use strict";var n=s("5ca1"),i=s("0a49")(2);n(n.P+n.F*!s("2f21")([].filter,!0),"Array",{filter:function(t){return i(this,t,arguments[1])}})},da26:function(t,e,s){t.exports=s.p+"img/img.a6cec5fc.jpg"},da8f:function(t,e,s){},e853:function(t,e,s){var n=s("d3f4"),i=s("1169"),a=s("2b4c")("species");t.exports=function(t){var e;return i(t)&&(e=t.constructor,"function"!=typeof e||e!==Array&&!i(e.prototype)||(e=void 0),n(e)&&(e=e[a],null===e&&(e=void 0))),void 0===e?Array:e}}}]);