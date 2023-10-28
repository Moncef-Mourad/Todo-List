const monthNumberMap = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
};

generateDatePicker();




// Function to generate the date picker
function generateDatePicker() {
    const yearElement = document.getElementById('year');
    const monthElement = document.getElementById('month');
    const dayElement = document.getElementById('day');
    const calendar = document.getElementById('calendar');

    const today = new Date();
    const currentYear = today.getFullYear();

    // Function to generate a list of days
    function generateDaysGrid() {
        const daysGrid = document.createElement('div');
        daysGrid.classList.add('calendar-grid');
        for (let i = 1; i <= 31; i++) {
            const dayButton = document.createElement('button');
            dayButton.classList.add('day-btn');
            dayButton.textContent = i;
            dayButton.addEventListener('click', () => {
                if (i < 10) dayElement.textContent = '0'+i;
                else dayElement.textContent = i;
                calendar.style.display = 'none';
            });
            daysGrid.appendChild(dayButton);
        }
        return daysGrid;
    }
    // Function to generate a list of months
    function generateMonthsGrid() {
        const monthsGrid = document.createElement('div');
        monthsGrid.classList.add('calendar-grid');
        const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        for (let i = 0; i < 12; i++) {
            const monthButton = document.createElement('button');
            monthButton.classList.add('month-btn');
            monthButton.textContent = monthNames[i];
            monthButton.addEventListener('click', () => {
                monthElement.textContent = monthNames[i];
                calendar.style.display = 'none';
            });
            monthsGrid.appendChild(monthButton);
        }
        return monthsGrid;
    }
    // Function to generate a list of years
    function generateYearsGrid() {
        const yearsGrid = document.createElement('div');
        yearsGrid.classList.add('calendar-grid');
        for (let i = currentYear; i <= currentYear + 12; i++) {
            const yearButton = document.createElement('button');
            yearButton.classList.add('year-btn');
            yearButton.textContent = i;
            yearButton.addEventListener('click', () => {
                yearElement.textContent = i;
                calendar.style.display = 'none';
            });
            yearsGrid.appendChild(yearButton);
        }
        return yearsGrid;
    }





    // Function to show the calendar below the clicked button
    function showCalendarBelowButton(button, grid) {
        const rect = button.getBoundingClientRect();
        grid.style.position = 'absolute';
        grid.style.top = rect.bottom + 'px';
        grid.style.left = rect.left + 'px';
        grid.style.display = 'block';
    }





    yearElement.addEventListener('click', () => {
        calendar.innerHTML = '';
        calendar.appendChild(generateYearsGrid());
        calendar.style.display = 'block';
        showCalendarBelowButton(yearElement, calendar);

            // Use a loop to add the event listener to each year button
    const yearBtns = document.getElementsByClassName('year-btn');
    for (const yearBtn of yearBtns) {
        yearBtn.addEventListener('click', () => {
        const newYear = yearBtn.textContent;
        const urlParts = window.location.pathname.split('/');
        urlParts[urlParts.length - 4] = newYear;
        const updatedURL = urlParts.join('/');
        console.log(updatedURL);
        window.location.assign(updatedURL);
    });
    }

    });




    monthElement.addEventListener('click', () => {
        calendar.innerHTML = '';
        calendar.appendChild(generateMonthsGrid());
        calendar.style.display = 'block';
        showCalendarBelowButton(monthElement, calendar);
            // Use a loop to add the event listener to each year button
            const monthBtns = document.getElementsByClassName('month-btn');
            for (const monthBtn of monthBtns) {
                monthBtn.addEventListener('click', () => {
                const newMonth = monthBtn.textContent;
                const monthNumber = monthNumberMap[newMonth];
                const urlParts = window.location.pathname.split('/');
                urlParts[urlParts.length - 3] = monthNumber;
                const updatedURL = urlParts.join('/');
                console.log(updatedURL);
                window.location.assign(updatedURL);
            });
        }
    });




    dayElement.addEventListener('click', () => {
        calendar.innerHTML = '';
        calendar.appendChild(generateDaysGrid());
        calendar.style.display = 'block';
        // calendar.style.backgroundColor = 'gray';
        showCalendarBelowButton(dayElement, calendar);

        // Use a loop to add the event listener to each year button
        const dayBtns = document.getElementsByClassName('day-btn');
        for (const dayBtn of dayBtns) {
            dayBtn.addEventListener('click', () => {
            const newDay = dayBtn.textContent;
            const urlParts = window.location.pathname.split('/');
            urlParts[urlParts.length - 2] = newDay;
            const updatedURL = urlParts.join('/');
            console.log(updatedURL);
            window.location.assign(updatedURL);
        });
    }
    });


    // Close the calendar when clicking outside
    document.addEventListener('click', (e) => {
        if (!calendar.contains(e.target) && e.target !== yearElement && e.target !== monthElement && e.target !== dayElement) {
            calendar.style.display = 'none';
        }
    });


}
