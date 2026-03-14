document.addEventListener("DOMContentLoaded", () => {

    const categoryNode = document.getElementById("category-data");
    const monthlyNode = document.getElementById("monthly-data");

    if (!categoryNode || !monthlyNode) return;

    const categoryData = JSON.parse(categoryNode.textContent || "[]");
    const monthlyData = JSON.parse(monthlyNode.textContent || "[]");

    /* =============================
       PIE CHART (CATEGORY SPENDING)
    ============================== */

    const pieCanvas = document.getElementById("categoryPie");

    if (pieCanvas) {

        new Chart(pieCanvas, {

            type: "pie",

            data: {
                labels: categoryData.map(row => row.category),

                datasets: [{
                    data: categoryData.map(row => row.total),

                    backgroundColor: [
                        "#1dd1a1",
                        "#54a0ff",
                        "#f368e0",
                        "#feca57",
                        "#ff6b6b",
                        "#5f27cd",
                        "#8395a7"
                    ],

                    borderWidth: 1
                }]
            },

            options: {
                responsive: true,

                plugins: {

                    legend: {
                        position: "bottom",
                        labels: {
                            font: {
                                family: "Inter"
                            }
                        }
                    },

                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `₱${context.raw.toFixed(2)}`;
                            }
                        }
                    }

                }

            }

        });

    }


    /* =============================
       LINE CHART (MONTHLY TREND)
    ============================== */

    const lineCanvas = document.getElementById("monthlyLine");

    if (lineCanvas) {

        new Chart(lineCanvas, {

            type: "line",

            data: {

                labels: monthlyData.map(row => row.month),

                datasets: [{
                    label: "Monthly Spend",

                    data: monthlyData.map(row => row.total),

                    borderColor: "#2a6ddf",
                    backgroundColor: "rgba(42,109,223,0.15)",

                    fill: true,

                    tension: 0.35,

                    pointRadius: 4,
                    pointBackgroundColor: "#2a6ddf"
                }]
            },

            options: {

                responsive: true,

                plugins: {

                    legend: {
                        display: true,
                        labels: {
                            font: {
                                family: "Inter"
                            }
                        }
                    }

                },

                scales: {

                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => "₱" + value
                        }
                    }

                }

            }

        });

    }

});