import pyproj
import verde as vd
import numpy as np
import matplotlib.pyplot as plt

print("Verde version:", vd.version.full_version)

data = vd.datasets.fetch_baja_bathymetry()
projection = pyproj.Proj(proj="merc", lat_ts=data.latitude.mean())
proj_coords = projection(data.longitude.values, data.latitude.values)

spacing = 10 / 60
interp = vd.Chain(
    [
        ("median", vd.BlockReduce(np.median, spacing=spacing * 111e3)),
        ("spline", vd.Spline(mindist=10e3, damping=1e-5)),
    ]
)
interp.fit(proj_coords, data.bathymetry_m)

grid = interp.grid(spacing=spacing * 111e3, data_names=["bathymetry"])
grid = vd.distance_mask(proj_coords, maxdist=30e3, grid=grid)

fig, ax = plt.subplots(1, 1, figsize=(7, 6))
pc = grid.bathymetry.plot.pcolormesh(ax=ax, cmap="viridis", vmax=0, add_colorbar=False)
plt.colorbar(pc, pad=0, ax=ax, aspect=40).set_label("bathymetry (m)")
ax.set_xlabel("Easting (m)")
ax.set_ylabel("Northing (m)")
ax.set_title("Gridded bathymetry")
ax.set_aspect("equal")
plt.show()
