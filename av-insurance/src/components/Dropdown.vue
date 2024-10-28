<template>
    <div class="nav-item dropdown" @mouseover="toggleDropdown" >
        <button style="background-color: transparent;border: none;" class="nav-link arrow-none"
         aria-haspopup="true" aria-expanded="false">
            <i class="feather-briefcase mr-2"></i>{{ defaultText }} <div class="arrow-down"></div>
        </button>
        <div v-if="() => (isOpen || onElements)" @mouseover="toggleElements" class="dropdown-menu">
            <a v-for="(item, index) in items" :key="index" :href="item.url" class="dropdown-item">
                {{ item.text }}
            </a>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'Dropdown',
    props: {
        items: {
            type: Array,
            required: true,
            // Each item should be an object with a `text` and `url` property
            default: () => []
        },
        defaultText: {
            type: String,
            default: 'Select an option'
        }
    },
    setup() {
        const onElements = ref(false);
        const isOpen = ref(false);

        const toggleDropdown = () => {
            isOpen.value = !isOpen.value;
        };
        const toggleElements = () => {
            onElements.value = !onElements.value;
        }

        return {
            isOpen,
            toggleDropdown,
            toggleElements,
            onElements
        };
    }
};
</script>
<style>
@import "../assets/css/bootstrap.min.module.css";
@import "../assets/css/icons.min.module.css";
@import "../assets/css/theme.min.module.css";


</style>
<!-- 
<template>
    <div class="dropdown-1" @mouseover="toggleDropdown">
        <button class="dropdown-button">{{ defaultText }}</button>
        <div v-if="isOpen" class="dropdown-menu-2">
            <a @mouseover="toggleDropdown" v-for="(item, index) in items" :key="index" :href="item.url" class="dropdown-item-1">
                {{ item.text }}
            </a>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'Dropdown',
    props: {
        items: {
            type: Array,
            required: true,
            // Each item should be an object with a `text` and `url` property
            default: () => []
        },
        defaultText: {
            type: String,
            default: 'Select an option'
        }
    },
    setup() {
        const onElements = ref(false);
        const isOpen = ref(false);

        const toggleDropdown = () => {
            isOpen.value = !(isOpen.value) || onElements.value;
        };
        const toggleElements = () => {
            onElements.value = !onElements.value;
            isOpen.value = isOpen.value ? isOpen.value : !isOpen.value;
        }

        return {
            isOpen,
            toggleDropdown,
            toggleElements,
            onElements
        };
    }
};
</script>

<style scoped>
.dropdown-1 {
    position: relative;
    display: inline-block;
}

.dropdown-button {
    padding: 10px 20px;
    border: 1px solid #ccc;
    cursor: pointer;
    background-color: #f9f9f9;
}

.dropdown-menu-2 {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background-color: white;
    border: 1px solid #ddd;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.dropdown-item-1 {
    padding: 10px;
    display: block;
    color: #333;
    text-decoration: none;
}

.dropdown-item:hover {
    background-color: #f1f1f1;
}
</style> -->