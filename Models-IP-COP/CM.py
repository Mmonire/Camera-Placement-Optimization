import random
import time

def read_data(file_path):
    """Reads input data from a file."""
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
            cameras[camera_id] = coverage

    return points, cameras

def evaluate_solution(solution, cameras, points):
    """Evaluate the solution by checking the coverage of points and counting the cameras used."""
    covered_points = set()
    unique_cameras = set(solution)

    for camera in unique_cameras:
        if camera in cameras:
            covered_points.update(cameras[camera])

    uncovered_points = set(points) - covered_points
    return len(unique_cameras), len(uncovered_points)

def generate_initial_solution(cameras, points):
    """Generate an initial random solution that covers all points."""
    solution = []
    covered_points = set()

    while len(covered_points) < len(points):
        random_camera = random.choice(list(cameras.keys()))
        solution.append(random_camera)
        covered_points.update(cameras[random_camera])

    return solution

def tabu_search(cameras, points, max_iter=100, tabu_size=10, aspiration_criteria=True):
    """Perform the Tabu Search algorithm to optimize the camera selection for covering all points."""
    current_solution = generate_initial_solution(cameras, points)
    best_solution = current_solution[:]
    best_cost, uncovered_points = evaluate_solution(best_solution, cameras, points)
    tabu_list = []
    aspiration_uses = 0

    output_file = "tabu_search_log.txt"
    with open(output_file, 'w') as file:
        file.write("Iteration\tBest Cost\tTabu Violations\tAspiration Uses\n")

    for iteration in range(1, max_iter + 1):
        neighborhood = []

        for camera in cameras.keys():
            neighbor = set(current_solution)
            if camera in neighbor:
                neighbor.remove(camera)
            else:
                neighbor.add(camera)

            if evaluate_solution(list(neighbor), cameras, points)[1] == 0:
                neighborhood.append(list(neighbor))

        best_neighbor = None
        best_eval = float('inf')
        tabu_violations = 0

        for neighbor in neighborhood:
            eval_solution = evaluate_solution(neighbor, cameras, points)

            if neighbor not in tabu_list or (aspiration_criteria and eval_solution[0] < best_cost):
                if eval_solution[0] < best_eval:
                    best_eval = eval_solution[0]
                    best_neighbor = neighbor

        if best_neighbor:
            current_solution = best_neighbor[:]
            current_cost, _ = evaluate_solution(current_solution, cameras, points)

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
            else:
                tabu_violations += 1

        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        with open(output_file, 'a') as file:
            file.write(f"{iteration}\t{best_cost}\t{tabu_violations}\t{aspiration_uses}\n")

    return best_solution, best_cost, aspiration_uses

#برای اجرا کافیست اسم نمونه اینجا درج شود و نمونه و کد داخل یک فصا باشند
data_file = "p12-c6.txt"
points, cameras = read_data(data_file)

start_time = time.time()
best_solution, best_cost, aspiration_uses = tabu_search(cameras, points, max_iter=500, tabu_size=20)
end_time = time.time()

unique_cameras = list(set(best_solution))
print("Selected Cameras:", unique_cameras)
print("Number of Cameras Selected:", len(unique_cameras))
print("Execution Time: {:.2f} seconds".format(end_time - start_time))
print("Aspiration Uses:", aspiration_uses)
