// function randsArray(length, min, max) {
//     return [...Array(length).keys()].map(() => {return Math.random() * (max - min) + min});
// }

// function bubblesDict(length, xmin, xmax, ymin, ymax, rmin, rmax) {
//     return [...Array(length).keys()].map(() => {return {x: Math.random() * (xmax - xmin) + xmin, y: Math.random() * (ymax - ymin) + ymin, r: Math.random() * (rmax - rmin) + rmin}});
// }

// function alphabetsArray(length) {
//     return [...Array(length).keys()].map((i) => {return String.fromCharCode('A'.charCodeAt(0) + i)});
// }

// const DATA_COUNT = 7;
// const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};

// const dataset1 = randsArray(DATA_COUNT, NUMBER_CFG['min'], NUMBER_CFG['max']);
// const dataset2 = randsArray(DATA_COUNT, NUMBER_CFG['min'], NUMBER_CFG['max']);
// const dataset3 = bubblesDict(DATA_COUNT, NUMBER_CFG['min'], NUMBER_CFG['max'], NUMBER_CFG['min'], NUMBER_CFG['max'], 1, 10);
// const dataset4 = bubblesDict(DATA_COUNT, NUMBER_CFG['min'], NUMBER_CFG['max'], NUMBER_CFG['min'], NUMBER_CFG['max'], 1, 10);


const data1 = {
    labels: chartLabels,
    datasets: [
        {
            label: 'Dataset 1',
            data: listChartDataX[0],
            borderWidth: 2,
            borderColor: 'rgba(255, 127, 191, 1)',
            backgroundColor: 'rgba(255, 127, 191, 0.5)',
        },
        {
            label: 'Dataset 2',
            data: listChartDataX[1],
            borderWidth: 2,
            borderColor: 'rgba(127, 255, 255, 1)',
            backgroundColor: 'rgba(127, 255, 255, 0.5)',
        }
    ]
};

const data2 = {
    labels: chartLabels,
    datasets: [
        {
            label: 'Dataset 3',
            data: listChartDataXYR[0],
            borderWidth: 2,
            borderColor: 'rgba(255, 191, 127, 1)',
            backgroundColor: 'rgba(255, 191, 127, 0.5)',
        },
        {
            label: 'Dataset 4',
            data: listChartDataXYR[1],
            borderColor: 'rgba(127, 255, 127, 1)',
            backgroundColor: 'rgba(127, 255, 127, 0.5)',
        }
    ]
};

const data3 = {
    labels: chartLabels,
    datasets: [
        {
            label: 'Dataset 1',
            data: listChartDataX[0],
            borderColor: 'rgba(255, 127, 191, 1)',
            backgroundColor: 'rgba(255, 127, 191, 0.5)',
            fill: 'origin',
        },
        {
            label: 'Dataset 2',
            data: listChartDataX[1],
            borderColor: 'rgba(127, 255, 255, 1)',
            backgroundColor: 'rgba(127, 255, 255, 0.5)',
            fill: 'origin',
        }
    ]
};

// BarChart
const configBar = {
    type: 'bar',
    data: data1,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: false,
                text: 'Vertical Bar Chart'
            }
        }
    },
};

const barChart = new Chart(
    document.getElementById('barChart'),
    configBar
);

// LineChart
const configLine = {
    type: 'line',
    data: data1,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: false,
                text: 'Line Chart'
            }
        }
    },
};

const lineChart = new Chart(
    document.getElementById('lineChart'),
    configLine
);

// BubbleChart
const configBubble = {
    type: 'bubble',
    data: data2,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: false,
                text: 'Bubble Chart'
            }
        }
    },
};

const bubbleChart = new Chart(
    document.getElementById('bubbleChart'),
    configBubble
);

// AreaChart
const configArea = {
    type: 'line',
    data: data3,
    options: {
        plugins: {
            filler: {
                propagate: false,
            },
            title: {
                display: false,
                text: 'Area Chart'
            }
        },
    },
};

const areaChart = new Chart(
    document.getElementById('areaChart'),
    configArea
);
