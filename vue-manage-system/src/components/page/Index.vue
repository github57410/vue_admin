<template>
<el-dropdown>
  <el-button type="primary">
    新闻分类<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <el-dropdown-menu slot="dropdown">
    <el-dropdown-item>历史新闻</el-dropdown-item>
    <el-dropdown-item>政要新闻</el-dropdown-item>
    <el-dropdown-item>军事新闻</el-dropdown-item>
    <el-dropdown-item>国内新闻</el-dropdown-item>
    <el-dropdown-item>国外新闻</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
</template>
<template>
    <div>我是shopcontent详情页面
        <h2 v-html="list.title"></h2>
        <div v-html="list.content"></div>
    </div>

</template>



<style>
  .el-dropdown {
    vertical-align: top;
  }
  .el-dropdown + .el-dropdown {
    margin-left: 15px;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }

</style>

<script>
  export default {
    methods: {
      handleClick() {
        alert('button click');
      }
    }
  }
</script>