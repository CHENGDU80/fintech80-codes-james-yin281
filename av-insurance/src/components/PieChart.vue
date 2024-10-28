<template>
    <div>
        <canvas class="pieChartClass" ref="pieChart"></canvas>
    </div>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
    name: 'PieChart',
    props: {
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
    methods: {
        createChart() {
            if (this.chartInstance) {
                this.chartInstance.destroy();
            }

            const ctx = this.$refs.pieChart.getContext('2d');
            this.chartInstance = new Chart(ctx, {
                type: 'pie',
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
    /* max-width: 100%; */
    /* border: solid green 1px; */
    height: auto;
}
.pieChartClass {
    max-width:min-content;
}
</style>