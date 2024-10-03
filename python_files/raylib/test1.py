from raylib import *

def main():
    InitWindow(800, 450, "Raylib Camera Example".encode('utf-8'))

    camera = Camera()
    camera.position = Vector3(0.0, 10.0, 10.0)  # Camera position
    camera.target = Vector3(0.0, 0.0, 0.0)     # Camera target (what it's looking at)
    camera.up = Vector3(0.0, 1.0, 0.0)         # Camera up vector

    SetCameraMode(camera, CAMERA_ORBITAL)  # Set the camera mode

    while not WindowShouldClose():
        UpdateCamera(byref(camera))  # Update camera position based on user input

        BeginDrawing()
        ClearBackground(RAYWHITE)

        BeginMode3D(camera)  # Start drawing in 3D using the camera
        DrawCube(Vector3(0.0, 0.0, 0.0), 2.0, 2.0, 2.0, RED)
        DrawGrid(20, 1.0)
        EndMode3D() 

        DrawFPS(10, 10)
        EndDrawing()

    CloseWindow()

if __name__ == "__main__":
    main()