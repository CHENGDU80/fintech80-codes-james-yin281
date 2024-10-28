<template>
    <!-- <div class="outbox"> -->
        <div style="display:flex; flex-wrap: wrap; justify-content: center;">
            <SmallCard title="Policy Sold" :price="dashboard_data['Policy Sold'].number" :pourcentage="trend(dashboard_data['Policy Sold'].display_data)">
                <sparkline :data="dashboard_data['Policy Sold'].display_data"></sparkline>
            </SmallCard>
            <SmallCard title="Total Premium" :price="dashboard_data['Total Premium'].number" :pourcentage="trend(dashboard_data['Total Premium'].display_data)" suffix="$">
                <sparkline :data="dashboard_data['Total Premium'].display_data"></sparkline>
            </SmallCard>
            <SmallCard title="Insured Amount" :price="dashboard_data['Insured Amount'].number" :pourcentage="trend(dashboard_data['Insured Amount'].display_data)" suffix="$">
                <sparkline :data="dashboard_data['Insured Amount'].display_data"></sparkline>
            </SmallCard>
            <SmallCard title="Policy Renewal Rate" :price="dashboard_data['Policy Renewal Rate'].number" :pourcentage="trend(dashboard_data['Policy Renewal Rate'].display_data)">
                <sparkline colo :data="dashboard_data['Policy Renewal Rate'].display_data"></sparkline>
            </SmallCard>
        </div>
        <div style="display:flex; justify-content: center;">
            <CardVue style="display:flex;" title="Insured Amount By Manufacturer" description="The comparative total insurance per compagny relative to each other">
                <ChartComponent chartType="doughnut" :chartData="pieData" :chartOptions="pieOptions" />
            </CardVue>
            <CardVue style="display:flex;" title="Number of Policies per Channel" description="Literal number of policies reported by channel type">
                <ChartComponent chartType="doughnut" :chartData="pieData2" :chartOptions="pieOptions2" />
            </CardVue>
        </div>
    <!-- </div> -->
</template>
<script>
import BarChart from '@/components/BarChart.vue';
import ChartComponent from '@/components/ChartComponent.vue';
import PieChart from '@/components/PieChart.vue';
import SmallCard from '@/components/SmallCard.vue';
import CardVue from '@/components/Card.vue';
import Sparkline from '@/components/Sparkline.vue';

const dashboard_data = {
    "Policy Sold": {
        display_data: [  0.,   4.,  66., 135., 105., 157., 105., 115., 136., 124., 201.,
        125., 223., 163., 165., 246., 231., 252., 173., 193., 213., 270.,
        288., 265., 245., 238., 256., 280., 256., 279., 237., 254., 330.,
        337., 310., 265.],
        number: 8261
    },
    "Total Premium": {
        display_data: [ 3909.31, 25619.84, 23574.62, 26104.24,  2474.  , 29060.47,
           0.  , 37064.32, 39270.2 ,  2158.21, 26613.98, 10454.97,
       15616.48,  2981.21,  2601.05, 29534.01, 20117.48, 35232.48,
       33950.63, 23700.06, 45931.84, 54761.04, 46234.83, 23261.92,
       56832.53, 18523.92, 40305.82, 52106.36, 41812.06, 23232.35,
        9975.34, 31308.64, 19991.56, 25202.55, 55646.71, 39138.24],
        number: 993809.95
    },
    "Insured Amount" : {
        display_data: [ 248575.5 ,  396183.18,  864918.46,  460777.72,  397625.94,
        310893.56,  130608.35,  752568.81,  365149.92,  157784.11,
        349371.53,   38219.87,  115671.58,       0.  ,  250519.6 ,
        974899.68,  403272.91, 1060237.22,  479765.49,  787098.72,
        540815.3 , 1224816.91,  594175.52,  366397.71,  820193.47,
        785638.78, 1196345.57,  834026.87, 1170149.93,  229612.06,
        248076.12,  500850.15,   32576.45,  472385.1 ,  885048.64,
        1090888.77],
        number: 15224585.93
    },
    "Policy Renewal Rate": {
        display_data: [83.74, 84.33, 74.29, 87.2 , 89.33, 92.67, 80.78, 73.92, 75.27,
            85.32, 79.94, 70.43, 79.29, 91.51, 84.84, 70.57, 79.09, 78.53,
            88.67, 72.86, 87.  , 70.63, 85.06, 90.62, 86.12, 92.81, 71.51,
            70.01, 87.04, 84.  , 91.91, 77.38, 89.78, 93.98, 90.31, 87.33],
        number: 87.33
    },
    "Insured Amount By Manufacturer": {
        labels: ['Audi', 'BMW', 'BYD', 'Li Auto', 'Mercedes-Benz', 'NIO', 'Tesla', 'XPeng'],
        data: [19273.46, 30183.69000000001, 22277.039999999997, 3113.2400000000002, 26438.189999999988, 2088.9500000000003, 15742.209999999994, 924.89]   
    },
    "Number of Policies per Channel": {
        labels: ['4S Stores', 'Online', 'In-Vehicule Infotainment System', 'Agent'],
        data: [390, 306, 176, 128]
    }

}

const COLORS = [
    '#4dc9f6',
    '#f67019',
    '#f53794',
    '#537bc4',
    '#acc236',
    '#166a8f',
    '#00a950',
    '#58595b',
    '#8549ba'
];

export default {
    components: { BarChart, PieChart, SmallCard, ChartComponent, CardVue, Sparkline },
    data() {
        return {
            dashboard_data : dashboard_data,
            pieData: {
                labels: dashboard_data["Insured Amount By Manufacturer"].labels,
                datasets: [
                    {
                        // label: "Dataset 1",
                        data: dashboard_data["Insured Amount By Manufacturer"].data,
                        backgroundColor: COLORS
                    }
                ],
            },
            pieOptions: {
                maintainAspectRatio: false,
            },
            pieData2: {
                labels: dashboard_data["Number of Policies per Channel"].labels,
                datasets: [
                    {
                        // label: "Dataset 1",
                        data: dashboard_data["Number of Policies per Channel"].data,
                        backgroundColor: COLORS
                    }
                ],
            },
            pieOptions2: {
                maintainAspectRatio: false,
            }
        }
    },
    methods: {
        trend(data) {
            data = Array.from(data)
            var tot = 0;
            for (let step = 0;  step < data.length - 1; step++) {
                tot += data[step + 1] - data[step]
            }
            // console.log(data)
            return `${tot >= 0 ? '+' : '-'}${Math.round(tot / (data.length - 1))}`
        }
    },
};
</script>
<style>
#size_element {
    width: fit-content;
}

.grid_display {
    /* display: flex; */
    /* justify-content: center; */
    /* justify-items: center; */
    /* flex-direction: row; */
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

.outbox {
    margin-block: 50px;
    margin-inline: 150px;
}
</style>