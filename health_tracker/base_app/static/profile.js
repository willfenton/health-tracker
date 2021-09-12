const app = new Vue({
    el: '#app',
    data: {
        events: [],
        users: [],
        user: {},
        points: 0,
        streak: 0,
        activities: [
            {
                name: 'Meditate',
                color: '#00aaee'
            },
            {
                name: 'Exercise',
                color: '#f70d1a'
            },
            {
                name: 'Socialize',
                color: '#ffe302'
            },
            {
                name: 'Get enough sleep',
                color: '#ff5f00'
            },
            {
                name: 'Eat healthy',
                color: '#9f00ff'
            },
        ],
    },
})

const pointsChart = new Chart(
    document.getElementById('points-canvas'), {
        type: 'line',
        data: {
            labels: [],
            datasets: []
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: {
                display: true
            }
        }
    })

const streakChart = new Chart(
    document.getElementById('streak-canvas'), {
        type: 'line',
        data: {
            labels: [],
            datasets: []
        }
    })

// Needed for axios requests to work
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// Get userId from HTML
const userId = parseInt(document.getElementById('userId').value)

const resetDateTimeSelects = () => {
    const dateSelect = document.getElementById('date')
    const timeSelect = document.getElementById('time')

    const now = Date.today().setTimeToNow()

    dateSelect.value = now.toString('yyyy-MM-dd')
    timeSelect.value = now.toString('HH:mm')
}

const trackActivity = () => {
    const activitySelect = document.getElementById('activity')
    const dateSelect = document.getElementById('date')
    const timeSelect = document.getElementById('time')

    const activity = activitySelect.value
    const date = dateSelect.value
    const time = timeSelect.value

    axios.post('/events/', {
        withCredentials: true,
        'userId': userId,
        'activity_date': `${date} ${time}`,
        'activity': activity,
        'points': 50
    })
        .then((response) => {
            refreshData()
        })
        .catch((error) => {
            console.error(error)
        })
}

const refreshData = () => {
    // get users
    axios.get('/users/')
        .then((response) => {
            app.users = response.data
            app.user = response.data.find((user) => user.id === userId)
        })
        .catch((error) => {
            console.error(error)
        })

    // get events
    axios.get('/events/')
        .then((response) => {
            const now = new Date().setTimeToNow()

            // get events only for the user
            let eventsForUser = response.data.filter((event) => event.userId === userId);

            // sort by date
            eventsForUser.forEach((event) => event.date = Date.parse(event.activity_date))

            // filter out future events
            eventsForUser = eventsForUser.filter((event) => now.getTime() - event.date.getTime() > 0)

            app.events = eventsForUser.sort((a, b) => Date.compare(b.date, a.date))

            // calculate points
            app.points = app.events.map((event) => event.points).reduce((a, b) => a + b, 0)

            resetPointsChart()
            resetStreakChart()
        })
        .catch((error) => {
            console.error(error)
        })
}

const resetPointsChart = () => {
    const datasets = app.activities.slice().concat({
        name: 'Total',
        color: '#56d837'
    })

    // sort earliest date to latest
    const events = app.events.slice().sort((a, b) => Date.compare(a.date, b.date))

    pointsChart.data.datasets = []

    datasets.forEach(({color, name}) => {
        const chartData = []

        let pointTotal = 0
        events.forEach((event) => {
            if (event.activity === name || name === "Total") {
                pointTotal += event.points
                chartData.push({
                    x: event.date.getTime(),
                    y: pointTotal
                })
            }
        })

        if (chartData.length > 0) {
            // chartData.push({
            //     x: new Date().setTimeToNow().getTime(),
            //     y: pointTotal
            // })

            pointsChart.data.datasets.push({
                data: chartData,
                label: name,
                borderColor: color,
                fill: false,
                lineTension: 0,
                hidden: name !== "Total"
            })
        }
    })

    pointsChart.update()
}

const resetStreakChart = () => {
    streakChart.update()
}

const searchForUser = () => {
    let profile_url = "http://127.0.0.1:8000/profile/";
    let username = document.getElementById("userSearch").value;
    let user_url = profile_url.concat("",username);
    let error_str = "user does not exist."
    let error_alert = username.concat(" ", error_str)

    var request = new XMLHttpRequest();  
    request.open('GET', user_url, true);
    request.onreadystatechange = function(){
        if (request.readyState === 4){
            if (request.status === 404) {  
                
                window.alert(error_alert);
            }else{
                location.href = user_url;
            }

        }
    };
    request.send();

}

refreshData()
