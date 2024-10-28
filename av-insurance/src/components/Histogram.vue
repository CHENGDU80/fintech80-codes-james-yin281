<template>
    <div class="histogram">
        <div v-for="(value, index) in data" :key="index" class="bar"
            :style="{ height: `${value}px`, backgroundColor: barColor }">
            <!-- <span class="label">{{ value }}</span> -->
        </div>
    </div>
</template>

<script>
export default {
    name: "Histogram",
    props: {
        data: {
            type: Array,
            required: true,
            default: () => [30, 70, 45, 60, 90, 40]
        },
        barColor: {
            type: String,
            default: "#4caf50"
        }
    }
};
</script>

<style scoped>
.histogram {
    display: flex;
    align-items: flex-end;
    justify-content: space-around;
    height: 200px;
    border-left: 2px solid #333;
    border-bottom: 2px solid #333;
    padding: 10px;
}

.bar {
    width: 20px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    position: relative;
}

.label {
    position: absolute;
    bottom: -20px;
    font-size: 12px;
    color: #333;
}
</style>