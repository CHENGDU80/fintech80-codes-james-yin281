<template>
    <div>
        <canvas ref="barChart"></canvas>
    </div>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
    name: 'BarChart',
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
            console.log(this.$refs)

            const ctx = this.$refs.barChart.getContext('2d');
            this.chartInstance = new Chart(ctx, {
                type: 'bar', // Set chart type to 'bar' for a vertical bar chart
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