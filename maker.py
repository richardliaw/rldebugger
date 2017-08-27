def make_gif_42(fname, trajectory)
    traj = np.array([s.reshape(42, 42) for s in trajectory]) * 255
    gif(fname, traj)
