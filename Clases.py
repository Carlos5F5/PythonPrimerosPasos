from alumnos import alumno
alumno1 = alumno("Juan", 22, "arquitectura", 7.1)
alumno2 = alumno("Carlos", 20, "Ingenieria", 10)

print(alumno1.nombre)
print(alumno1.aprobado())
print(alumno2.nombre, alumno2.edad, alumno2.carrera)