# sortuje dystanse rosnaco od najmniejszej do najwiekszej wartosci
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
sorted_distances = sorted(distances_traveled)
print("Distances traveled:", sorted_distances)

# sortuje temperatury malejaco dzieki dodaniu parametru reverse=True
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_temperatures = sorted(daily_temperatures, reverse=True)
print("Daily temperatures:", sorted_temperatures)

# sortuje nazwy plikow alfabetycznie od A do Z
file_names = [
    "report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
    "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"
]
sorted_files = sorted(file_names)
print("File names:", sorted_files)