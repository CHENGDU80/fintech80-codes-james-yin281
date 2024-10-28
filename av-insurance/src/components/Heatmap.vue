<template>
    <div>
        <l-map :zoom="zoom" :center="center" style="height: 600px; width: 100%">
            <l-tile-layer :url="tileLayer" :attribution="attribution" />
            <l-geo-json :geojson="usGeoJson" :options-style="styleFeature" @mouseover="highlightFeature"
                @mouseout="resetHighlight" />
        </l-map>
    </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";
import "leaflet/dist/leaflet.css";
import usGeoJson from "@/data/us-counties.json"; // Make sure to place your geoJSON here

export default {
    name: "USHeatmap",
    components: {
        LMap,
        LTileLayer,
        LGeoJson
    },
    props: {
        countyOccurrences: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            usGeoJson: usGeoJson,
            center: [37.8, -96],
            zoom: 4,
            tileLayer: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            countyCounts: {} // Object to store frequency of each county
        };
    },
    created() {
        this.calculateCountyCounts();
    },
    methods: {
        calculateCountyCounts() {
            // Initialize counts to zero for each county in geoJSON
            this.usGeoJson.features.forEach(feature => {
                const countyId = feature.properties.GEO_ID;
                this.countyCounts[countyId] = 0;
            });

            // Calculate appearance counts
            this.countyOccurrences.forEach(countyId => {
                if (this.countyCounts[countyId] !== undefined) {
                    this.countyCounts[countyId]++;
                }
            });
        },
        styleFeature(feature) {
            const countyId = feature.properties.GEO_ID;
            const count = this.countyCounts[countyId] || 0;

            return {
                fillColor: this.getColor(count),
                weight: 1,
                opacity: 1,
                color: "white",
                dashArray: "3",
                fillOpacity: 0.7
            };
        },
        getColor(count) {
            // Define color scales based on count
            return count > 100
                ? "#800026"
                : count > 50
                    ? "#BD0026"
                    : count > 20
                        ? "#E31A1C"
                        : count > 10
                            ? "#FC4E2A"
                            : count > 5
                                ? "#FD8D3C"
                                : count > 2
                                    ? "#FEB24C"
                                    : count > 0
                                        ? "#FED976"
                                        : "#FFEDA0";
        },
        highlightFeature(e) {
            const layer = e.target;
            layer.setStyle({
                weight: 3,
                color: "#666",
                fillOpacity: 0.9
            });
            layer.bringToFront();
        },
        resetHighlight(e) {
            const layer = e.target;
            layer.setStyle(this.styleFeature(layer.feature));
        }
    }
};
</script>

<style scoped>
/* Add styling if needed */
</style>