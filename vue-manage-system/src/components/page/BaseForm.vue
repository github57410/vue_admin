<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>基本表单</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="文章标题">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>
                    <el-form-item label="文件上传">
                        <el-button @click="xinZengF()">点击上传文章配图</el-button>
                    </el-form-item>
                    <el-form-item label="新闻类型">
                        <el-select v-model="form.region" placeholder="请选择">
                            <el-option key="bbk" label="历史新闻" value="bbk"></el-option>
                            <el-option key="xtc" label="政要新闻" value="xtc"></el-option>
                            <el-option key="junshi" label="军事新闻" value="junshi"></el-option>
                            <el-option key="guonei" label="国内新闻" value="guonei"></el-option>
                            <el-option key="guowai" label="国外新闻" value="guowai"></el-option>

                        </el-select>
                    </el-form-item>
                    <el-form-item label="发布日期时间">
                        <el-col :span="11">
                            <el-date-picker
                                type="date"
                                placeholder="选择日期"
                                v-model="form.date1"
                                value-format="yyyy-MM-dd"
                                style="width: 100%;"
                            ></el-date-picker>
                        </el-col>
                        <el-col class="line" :span="2">-</el-col>
                        <el-col :span="11">
                            <el-time-picker
                                placeholder="选择时间"
                                v-model="form.date2"
                                style="width: 100%;"
                            ></el-time-picker>
                        </el-col>
                    </el-form-item>
                    <el-form-item label="城市级联">
                        <el-cascader :options="options" v-model="form.options"></el-cascader>
                    </el-form-item>

                    <el-form-item label="文本框">
                        <el-input type="textarea" rows="5" v-model="form.desc"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">表单提交</el-button>
                        <el-button>取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'baseform',
    data() {
        return {
            options: [
                {
                    value: 'guangdong',
                    label: '广东省',
                    children: [
                        {
                            value: 'guangzhou',
                            label: '广州市',
                            children: [
                                {
                                    value: 'tianhe',
                                    label: '天河区'
                                },
                                {
                                    value: 'haizhu',
                                    label: '海珠区'
                                }
                            ]
                        },
                        {
                            value: 'dongguan',
                            label: '东莞市',
                            children: [
                                {
                                    value: 'changan',
                                    label: '长安镇'
                                },
                                {
                                    value: 'humen',
                                    label: '虎门镇'
                                }
                            ]
                        }
                    ]
                },
                {
                    value: 'hunan',
                    label: '湖南省',
                    children: [
                        {
                            value: 'changsha',
                            label: '长沙市',
                            children: [
                                {
                                    value: 'yuelu',
                                    label: '岳麓区'
                                }
                            ]
                        }
                    ]
                }
            ],
            form: {
                name: '', //文章标题
                region: '',  //文章类型
                date1: '',   //发布日期
                date2: '',  //发布时间

                options: []
            }
        };
    },
    methods: {
        onSubmit() {
            this.$message.success('提交成功！');

        },
        xinZengF(){
        this.$router.push('/upload');
        }
    },
    created () {
    this.axios.get('/')
      .then(function (response) {
        console.log(response)
      })
      .catch(function (response) {
        console.log(response)
      })
    }
};
</script>