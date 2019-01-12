<template>
 <div :id="id" :style="style"></div>
</template>
<script>
export default {
 name: "Chart",
 data() {
  return {
      // echarts实例
   chart: "" 
  };
 },
 props: {
      // 父组件需要传递的参数：id，width，height，option
  id: {
   type: String
  },
  width: {
    type: String,
    default: "100%"
  },
  height: {
   type: String,
   default: "300px"
  },
  option: {
   type: Object,
      // Object类型的prop值一定要用函数return出来，不然会报错。原理和data是一样的，
      // 使用闭包保证一个vue实例拥有自己的一份props
   default() {
    return {
        title: { text: '在Vue中使用echarts' },
        tooltip: {},
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line'
        }]
    };
   }
  }
 },
 computed: {
  style() {
   return {
    height: this.height,
    width: this.width
   };
  }
 },
 methods: {
  myinit() {
   this.chart = this.$echarts.init(document.getElementById(this.id));
   this.chart.setOption(this.option);
  }
 },
 mounted () {
  this.myinit();
 }
};
</script>