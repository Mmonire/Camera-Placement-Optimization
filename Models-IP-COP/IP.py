from docplex.mp.model import Model

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    points = []
    cameras = {}

    for line in lines:
        if line.startswith('points: '):
            points = line.strip().split(': ')[1].split(', ')
        elif line.startswith('c'):
            parts = line.strip().split(': ')
            camera_id = parts[0]
            coverage = parts[1].split(', ')
            cameras[camera_id] = {'coverage': coverage}

    return points, cameras

def optimize_camera_placement(data_file):
    # Read data
    points, cameras = read_data(data_file)

    # Debug: Check point coverage
    uncovered_points = [point for point in points if not any(point in cameras[camera]['coverage'] for camera in cameras)]
    if uncovered_points:
        print("Error: The following points are not covered by any camera:", uncovered_points)

    # Create the optimization model
    mdl = Model(name='Camera Placement Optimization')

    # Decision variables
    x = {camera: mdl.binary_var(name=f'x_{camera}') for camera in cameras}

    # Objective: Minimize the number of cameras used
    mdl.minimize(mdl.sum(x[camera] for camera in cameras))

    # Constraints: Ensure every point is covered by at least one camera
    for point in points:
        coverage_cameras = [camera for camera in cameras if point in cameras[camera]['coverage']]
        if coverage_cameras:
            mdl.add_constraint(mdl.sum(x[camera] for camera in coverage_cameras) >= 1,
                               ctname=f'cover_{point}')
        else:
            print(f"Warning: Point {point} is not covered by any camera!")

    # Solve the model
    solution = mdl.solve(log_output=True)

    # Display results
    if solution:
        # Calculate the number of selected cameras
        selected_cameras = [camera for camera in cameras if x[camera].solution_value > 0.5]
        num_selected_cameras = len(selected_cameras)

        print("Optimal Number of Cameras:", num_selected_cameras)
        print("Selected Cameras:")
        for camera in selected_cameras:
            print(f"  {camera}: Coverage={cameras[camera]['coverage']}")
    else:
        print("No solution found.")

# Input data file path
data_file = 'p12-c6.txt'

# Run the optimization
optimize_camera_placement(data_file)
