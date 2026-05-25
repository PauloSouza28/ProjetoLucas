document.addEventListener('DOMContentLoaded', function () {

    const canvas = document.getElementById(
        'graficoFinanceiro'
    );

    if (!canvas) return;

    const receitas = parseFloat(
    canvas.dataset.receitas.replace(',', '.')
);

const despesas = parseFloat(
    canvas.dataset.despesas.replace(',', '.')
);
    new Chart(canvas, {

        type: 'line',

        data: {

            labels: [
                'Jan',
                'Fev',
                'Mar',
                'Abr',
                'Mai',
                'Jun'
            ],

            datasets: [

                {
                    label: 'Receitas',

                    data: [
                        0,
                        receitas,
                        receitas,
                        receitas,
                        receitas,
                        receitas
                    ],

                    borderColor: '#22c55e',

                    backgroundColor: '#22c55e',

                    tension: 0.4
                },

                {
                    label: 'Despesas',

                    data: [
                        0,
                        despesas,
                        despesas,
                        despesas,
                        despesas,
                        despesas
                    ],

                    borderColor: '#ef4444',

                    backgroundColor: '#ef4444',

                    tension: 0.4
                }

            ]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    labels: {
                        color: 'white'
                    }
                }
            },

            scales: {

                x: {

                    ticks: {
                        color: 'white'
                    },

                    grid: {
                        color: '#334155'
                    }
                },

                y: {

                    ticks: {
                        color: 'white'
                    },

                    grid: {
                        color: '#334155'
                    }
                }
            }
        }
    });

});