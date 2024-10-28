<template>
<Card
    title="Car Status"
    description="Informations about the car"
    style="width:100%; display: flex; flex-direction: row;"
>
    <div v-for="item in Object.keys(selected_client || {})">
        <b>{{ item }}:</b></br> {{ selected_client[item] }}
    </div>
</Card>
</template>
<script>
import Card from '@/components/Card.vue'
// import { useRoute } from 'vue-router'

const client_names = [
    {
        client_id : 0,
        info: {
            name : "Thomas Brown"
        }
    },
    {
        client_id : 1,
        info: {
            name : "Jeffrey Torres"
        }
    },
    {
        client_id : 2,
        info: {
            name : "Tanya Chamber"
        }
    }
]

const car_informations = [
    {
        client_id : 0,
        info: {
            "Model" : "BYD Seal",
            "Autonomous Software" : "BYD Dipilot",
            "Sensors": "LiDAR",
            "Computing Units": "NVIDIA Orin",
            "Connectivity": "Bluetooth Adapter",
            "Power System" : "DC-DC Converter",
            "Braking System": "ABS Module",
            "Steering System" : "Electric Power Steering"  
        }
    },
    {
        client_id : 1,
        info: {
            "Model" : "Tesla Model X",
            "Autonomous Software" : "Tesla Full Self-Driving",
            "Sensors": "LiDAR",
            "Computing Units": "NVIDIA Orin",
            "Connectivity": "Bluetooth Adapter",
            "Power System" : "DC-DC Converter",
            "Braking System": "ABS Module",
            "Steering System" : "Electric Power Steering"  
        }
    },
    {
        client_id : 2,
        info: {
            "Model" : "Tesla Model X",
            "Autonomous Software" : "Tesla Full Self-Driving",
            "Sensors": "LiDAR",
            "Computing Units": "NVIDIA Orin",
            "Connectivity": "Bluetooth Adapter",
            "Power System" : "DC-DC Converter",
            "Braking System": "ABS Module",
            "Steering System" : "Electric Power Steering"  
        }
    }
]


export default {
    components: { Card },
    data() {
        return {
            selected_client: this.selected_client
        }
    },
    mounted() {
        this.selected_client = car_informations.filter(a => a.client_id == this.$route.params.id)[0].info
        // console.log(this.selected_client)
    }
}
</script>