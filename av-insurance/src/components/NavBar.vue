<template>
    <div class="topnav">
        <div class="container-fluid">
            <nav class="navbar navbar-dark navbar-expand-lg topnav-menu">

                <div class="collapse navbar-collapse" id="topnav-menu-content">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/dashboard">
                                <i class="feather-home mr-2"></i>Home
                            </a>
                        </li>

                        <Dropdown defaultText="Dashboard" :items="Routes"/>

                        <li class="nav-item">
                            <a class="nav-link" href="/generate-policy">
                                Generate Policy
                            </a>
                        </li>

                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle arrow-none" href="#" id="topnav-charts" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="feather-bar-chart-2 mr-2"></i>Charts <div class="arrow-down"></div>
                            </a>
                            <div class="dropdown-menu" aria-labelledby="topnav-charts">
                                <a href="charts-morris.html" class="dropdown-item">Morris</a>
                                <a href="charts-google.html" class="dropdown-item">Google</a>
                                <a href="charts-chartjs.html" class="dropdown-item">Chartjs</a>
                                <a href="charts-sparkline.html" class="dropdown-item">Sparkline</a>
                                <a href="charts-knob.html" class="dropdown-item">Jquery Knob</a>
                            </div>
                        </li>

                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle arrow-none" href="#" id="topnav-forms" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="feather-disc mr-2"></i>Forms <div class="arrow-down"></div>
                            </a>
                            <div class="dropdown-menu" aria-labelledby="topnav-forms">
                                <a href="forms-elements.html" class="dropdown-item">Elements</a>
                                <a href="forms-plugins.html" class="dropdown-item">Plugins</a>
                                <a href="forms-validation.html" class="dropdown-item">Validation</a>
                                <a href="forms-mask.html" class="dropdown-item">Masks</a>
                                <a href="forms-quilljs.html" class="dropdown-item">Quilljs</a>
                                <a href="forms-uploads.html" class="dropdown-item">File Uploads</a>
                            </div>
                        </li>

                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle arrow-none" href="#" id="topnav-more" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="feather-book-open mr-2"></i>More <div class="arrow-down"></div>
                            </a>
                            <div class="dropdown-menu" aria-labelledby="topnav-more">
                                <div class="dropdown">
                                    <a class="dropdown-item dropdown-toggle arrow-none" href="#" id="topnav-tables"
                                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        Tables <div class="arrow-down"></div>
                                    </a>
                                    <div class="dropdown-menu" aria-labelledby="topnav-tables">
                                        <a href="tables-basic.html" class="dropdown-item">Basic Tables</a>
                                        <a href="tables-datatables.html" class="dropdown-item">Data Tables</a>
                                    </div>
                                </div>
                                <a href="calendar.html" class="dropdown-item">Calendar</a>
                                <div class="dropdown">
                                    <a class="dropdown-item dropdown-toggle arrow-none" href="#" id="topnav-icons"
                                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        Icons <div class="arrow-down"></div>
                                    </a>
                                    <div class="dropdown-menu" aria-labelledby="topnav-icons">
                                        <a href="icons-feather.html" class="dropdown-item">Feather Icons</a>
                                        <a href="icons-materialdesign.html" class="dropdown-item">Material Design</a>
                                        <a href="icons-dripicons.html" class="dropdown-item">Dripicons</a>
                                        <a href="icons-fontawesome.html" class="dropdown-item">Font awesome</a>
                                    </div>
                                </div>
                                <div class="dropdown">
                                    <a class="dropdown-item dropdown-toggle arrow-none" href="#" id="topnav-maps"
                                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        Maps <div class="arrow-down"></div>
                                    </a>
                                    <div class="dropdown-menu" aria-labelledby="topnav-maps">
                                        <a href="maps-google.html" class="dropdown-item">Google Maps</a>
                                        <a href="maps-vector.html" class="dropdown-item">Vector Maps</a>
                                    </div>
                                </div>
                            </div>
                        </li>

                    </ul>
                </div>
            </nav>
        </div>
    </div>
</template>
<script>
import Dropdown from '@/components/Dropdown.vue';

const Routes = [
    {
        text: "Policy Overview",
        url: "/dashboard"
    },
    {
        text: "Policy Table",
        url: "/policy"
    },
    {
        text: "Claims overview",
        url: "/claims-overview"
    },
    {
        text: "Driver Behavior Analysis",
        url: "/driver"
    },
]

export default {
    components: { Dropdown },
    data() {
        return {
            Routes : Routes
        }
    }
}
</script>
<style>
@import "../assets/css/bootstrap.min.module.css";
@import "../assets/css/icons.min.module.css";
@import "../assets/css/theme.min.module.css";
</style>