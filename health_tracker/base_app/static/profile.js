// <form>
//     <div className="mb-3">
//         <label htmlFor="activity" className="form-label">Activity</label>
//         <select className="form-select" id="activity" required>
//             <option>Exercise</option>
//             <option>Eat healthy</option>
//             <option>Meditate</option>
//             <option>Get enough sleep</option>
//             <option>Socialize</option>
//         </select>
//     </div>
//     <div className="mb-3">
//         <label htmlFor="date" className="form-label">Date</label>
//         <input type="date" id="date" required>
//     </div>
//     <div className="mb-3">
//         <label htmlFor="time" className="form-label">Time</label>
//         <input type="time" id="time" required>
//     </div>
// </form>

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "XCSRF-TOKEN"

const activitySelect = document.getElementById('activity')
const dateSelect = document.getElementById('date')
const timeSelect = document.getElementById('time')

const trackActivity = () => {
    const activity = activitySelect.value
    const date = dateSelect.value
    const time = timeSelect.value
    console.log(activity, date, time)

    axios.post('/events/', {
        withCredentials: true,
        'userId': 3,
        'activity_date': `${date} ${time}`,
        'activity': activity,
        'points': 50
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}

