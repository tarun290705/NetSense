import numpy as np
from pso.particle import generate_particle
from pso.fitness import fitness_function

def run_pso(X_train, n_particles=5, n_iterations=5):
    particles = [generate_particle() for _ in range(n_particles)]
    pbest = particles.copy()
    pbest_scores = [float('inf')] * n_particles

    gbest = None
    gbest_score = float('inf')

    for iteration in range(n_iterations):
        print(f"PSO Iteration {iteration+1}/{n_iterations}")

        for i, particle in enumerate(particles):
            score = fitness_function(particle, X_train)

            if score < pbest_scores[i]:
                pbest_scores[i] = score
                pbest[i] = particle

            if score < gbest_score:
                gbest_score = score
                gbest = particle

        print("Best reconstruction loss:", gbest_score)

    return gbest
