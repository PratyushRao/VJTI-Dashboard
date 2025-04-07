
function toggleSubMenu() {
    const submenu = document.getElementById("semester-submenu");
    submenu.style.display = (submenu.style.display === "block") ? "none" : "block";
}

// Data for Subjects
const semesterSubjects = {
    1: [
        { name: "Chemistry", grade: "AA", attendance: "85%", faculty: "Dr. Vithal Kashid", credits: 3 },
        { name: "Maths", grade: "AA", attendance: "90%", faculty: "Dr. Shruti Parmar", credits: 3 },
        { name: "Basic Electrical Eng", grade: "AA", attendance: "85%", faculty: "Dr. Hmea Singh", credits: 2 },
        { name: "Bio Science Eng", grade: "AA", attendance: "95%", faculty: "Dr. NAME yyad nhi", credits: 2 },
        { name: "Engineering Mechanics", grade: "BB", attendance: "85%", faculty: "Dr. Komal Bedi", credits: 2 },
        { name: "Electrical Workshop", grade: "AA", attendance: "70%", faculty: "Dr. Shubhashini", credits: 1.50 }
    ],
    2: [
        { name: "Basic Electronics", grade: "AB", attendance: "70%", faculty: "Dr. Hmesha Lata", credits: 3 },
        { name: "Numerical Techniques", grade: "BB", attendance: "80%", faculty: "Dr. Zohra Khan", credits: 3 },
        { name: "Physics", grade: "AA", attendance: "95%", faculty: "Dr. Baliram Nandekar", credits: 4 },
        { name: "Maths", grade: "AA", attendance: "100%", faculty: "Dr. Shruti Parmar", credits: 3 },
        { name: "Engineering Graphics", grade: "CC", attendance: "95%", faculty: "Dr. Hasmukh", credits: 4 },
        { name: "Bussiness Technical Communication", grade: "AB", attendance: "98%", faculty: "Dr. Shama Sidiqui", credits: 4 }
    ],
};
// Announcement Data
const announcements = [
    {
        date: "11-March-2025",
        type: "Exam Alert",
        title: "Mid-Sem Exam Schedule",
        postedBy: "EED Department",
        attachment: "exam-schedule.pdf"
    },
    {
        date: "25-March-2025",
        type: "Notice",
        title: "Holiday on 31th March",
        postedBy: "Admin Office",
        attachment: ""
    },
    {
        date: "01-Apr-2025",
        type: "Update",
        title: "Seminar in Auditorium",
        postedBy: "Prof. Wagh",
        attachment: "seminar-schedule.pdf"
    },
    {
        date: "05-Apr-2025",
        type: "Notice",
        title: "Internship Period",
        postedBy: "TPO Department",
        attachment: "internship.pdf"
    }
];

const studentName = "Purvasha Singh"; 
document.getElementById("student-name").textContent = studentName;
document.getElementById("profile-name").textContent = studentName;

const regNumber = "VJTI241091060";
document.getElementById("profile-reg").textContent = regNumber; 
document.getElementById("student-reg").textContent = regNumber; 

function setActiveSidebar(linkId) {
    const sidebarLinks = document.querySelectorAll('.sidebar-menu li a');
    sidebarLinks.forEach(link => link.classList.remove('active'));
    document.getElementById(linkId).classList.add('active');
}

window.onload = function() {
    showProfile(); // Default page
    setActiveSidebar('profile-link'); // Highlight 'Profile'
};

function populateAnnouncements() {
    const tbody = document.getElementById("announcement-table-body");
    tbody.innerHTML = ""; 

    announcements.forEach(item => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${item.date}</td>
            <td>${item.type}</td>
            <td>${item.title}</td>
            <td>${item.postedBy}</td>
            <td>${
                item.attachment 
                ? `<a class="download-link" href="${item.attachment}" target="_blank">Download</a>` 
                : "—"
            }</td>
        `;

        tbody.appendChild(row);
    });
}

function hideAllSections() {
    document.getElementById("profile-container").style.display = "none";
    document.getElementById("download-container").style.display = "none";
    document.getElementById("subject-container").style.display = "none";
    document.getElementById("announcement-container").style.display = "none";
    document.getElementById("main-content").style.display = "block";
}

function showProfile() {
    hideAllSections();
    document.getElementById("page-title").innerText = "Welcome to Student Portal, Purvasha Singh!";
    document.getElementById("profile-container").style.display = "block";
}

function showDownloads() {
    hideAllSections();
    document.getElementById("page-title").innerText = "Download Resources";
    document.getElementById("download-container").style.display = "block";
}


function openSemester(semester) {
    hideAllSections();
    document.getElementById("page-title").innerText = `Semester ${semester} Subjects`;
    document.getElementById("subject-container").style.display = "flex";

    const subjectContainer = document.getElementById("subject-container");
    const subjects = semesterSubjects[semester];

    if (!subjects || subjects.length === 0) {
        subjectContainer.innerHTML = `
            <div class="no-subject-msg">
                ❌ NO SUBJECT FOUND
            </div>
        `;
        return;
    }

    const cardsHTML = subjects.map(sub => `
        <div class="subject-card">
            <h3>${sub.name}</h3>
            <p><strong>Grade:</strong> ${sub.grade}</p>
            <p><strong>Attendance:</strong> ${sub.attendance}</p>
            <p><strong>Faculty:</strong> ${sub.faculty}</p>
            <p><strong>Credits:</strong> ${sub.credits}</p>
        </div>
    `).join('');

    let totalCredits = 0;
    const tableRows = subjects.map(sub => {
        totalCredits += parseFloat(sub.credits);
        return `
            <tr>
                <td>${sub.name}</td>
                <td>${sub.credits}</td>
            </tr>`;
    }).join('');

    const tableHTML = `
        <div class="course-table-wrapper">
            <h3>Course & Credit Table</h3>
            <table class="course-table">
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>Credits</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                    <tr>
                        <td><strong>Total Credits</strong></td>
                        <td><strong>${totalCredits}</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>
    `;

    subjectContainer.innerHTML = cardsHTML + tableHTML;
}


function showAnnouncements() {
    hideAllSections();
    document.getElementById("sidebar").style.display = "block";
    document.getElementById("page-title").innerText = "Announcements";
    document.getElementById("announcement-container").style.display = "block";

    populateAnnouncements(); 
}


