<template>
    <div style="display: flex; flex-direction: column; align-content: end;">
      <canvas ref="chartCanvas"></canvas>
    </div>
</template>
  
  <script>
  import { Chart } from 'chart.js/auto';
  
  export default {
    name: 'ChartComponent',
    props: {
      chartType: {
        type: String,
        maxHeight : String,
        required: true,
        validator: (value) => ['line', 'bar', 'pie', 'doughnut', 'radar', 'polarArea'].includes(value),
      },
      chartData: {
        type: Object,
        required: true,
      },
      chartOptions: {
        type: Object,
        default: () => ({}),
      },
    },
    mounted() {
      this.createChart();
    },
    computed: {
      style () {
        return maxHeight ? 'canvas { max-height: ' + maxHeight + ';}' : '';
      }
    },
    methods: {
      createChart() {
        if (this.chartInstance) {
          this.chartInstance.destroy();
        }
  
        const ctx = this.$refs.chartCanvas.getContext('2d');
        this.chartInstance = new Chart(ctx, {
          type: this.chartType, // Use the passed chartType prop here
          data: this.chartData,
          options: this.chartOptions,
        });
      },
    },
    watch: {
      chartData: {
        deep: true,
        handler() {
          this.createChart();
        },
      },
    },
    beforeDestroy() {
      if (this.chartInstance) {
        this.chartInstance.destroy();
      }
    },
  };
  </script>
  
  <style scoped>
  canvas {
    max-width: 100%;
    height: auto;
  }
  </style>
  