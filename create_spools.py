#!/usr/bin/env python3
"""
Script to create fabrication spool sheets.
Generates plan view, isometric view, section view with dimensions and annotations,
along with BOM and legend for selected fabrication pipes.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

def create_plan_view(pipe_data, spool_name):
    """Create plan view (top view) of the spool."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f'Plan View - {spool_name}')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.grid(True)

    # Draw pipes as lines (simplified)
    for pipe in pipe_data:
        x1, y1, x2, y2 = pipe['start'][0], pipe['start'][1], pipe['end'][0], pipe['end'][1]
        ax.plot([x1, x2], [y1, y2], 'b-', linewidth=pipe['diameter']/10)
        # Add dimensions
        ax.annotate(f"{pipe['length']}mm", xy=((x1+x2)/2, (y1+y2)/2), xytext=(0, 10),
                    textcoords='offset points', ha='center')

    plt.axis('equal')
    plt.savefig(f'{spool_name}_plan.png')
    plt.close()

def create_isometric_view(pipe_data, spool_name):
    """Create isometric view of the spool."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(f'Isometric View - {spool_name}')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_zlabel('Z (mm)')

    # Draw pipes as 3D lines
    for pipe in pipe_data:
        x = [pipe['start'][0], pipe['end'][0]]
        y = [pipe['start'][1], pipe['end'][1]]
        z = [pipe['start'][2], pipe['end'][2]]
        ax.plot(x, y, z, 'b-', linewidth=pipe['diameter']/10)

    plt.savefig(f'{spool_name}_iso.png')
    plt.close()

def create_section_view(pipe_data, spool_name):
    """Create section view (side view) of the spool."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f'Section View - {spool_name}')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Z (mm)')
    ax.grid(True)

    # Draw pipes as lines in X-Z plane
    for pipe in pipe_data:
        x1, z1, x2, z2 = pipe['start'][0], pipe['start'][2], pipe['end'][0], pipe['end'][2]
        ax.plot([x1, x2], [z1, z2], 'b-', linewidth=pipe['diameter']/10)
        # Add dimensions
        ax.annotate(f"{pipe['length']}mm", xy=((x1+x2)/2, (z1+z2)/2), xytext=(0, 10),
                    textcoords='offset points', ha='center')

    plt.axis('equal')
    plt.savefig(f'{spool_name}_section.png')
    plt.close()

def create_bom(pipe_data, spool_name):
    """Create Bill of Materials."""
    with open(f'{spool_name}_bom.txt', 'w') as f:
        f.write(f'Bill of Materials - {spool_name}\n')
        f.write('=' * 40 + '\n')
        f.write('Item\tDescription\tQuantity\tLength (mm)\tDiameter (mm)\n')
        for i, pipe in enumerate(pipe_data, 1):
            f.write(f'{i}\tPipe\t1\t{pipe["length"]}\t{pipe["diameter"]}\n')

def create_legend(spool_name):
    """Create legend."""
    with open(f'{spool_name}_legend.txt', 'w') as f:
        f.write(f'Legend - {spool_name}\n')
        f.write('=' * 20 + '\n')
        f.write('Blue line: Pipe\n')
        f.write('Numbers: Length in mm\n')

def create_spool_sheet(pipe_data, spool_name):
    """Create complete spool sheet."""
    create_plan_view(pipe_data, spool_name)
    create_isometric_view(pipe_data, spool_name)
    create_section_view(pipe_data, spool_name)
    create_bom(pipe_data, spool_name)
    create_legend(spool_name)
    print(f'Spool sheet for {spool_name} created.')

# Sample data for demonstration
sample_pipes = [
    {'start': [0, 0, 0], 'end': [1000, 0, 0], 'length': 1000, 'diameter': 50},
    {'start': [1000, 0, 0], 'end': [1000, 500, 0], 'length': 500, 'diameter': 50},
    {'start': [1000, 500, 0], 'end': [1500, 500, 0], 'length': 500, 'diameter': 50},
]

if __name__ == '__main__':
    # Create directory for outputs
    os.makedirs('spool_sheets', exist_ok=True)
    os.chdir('spool_sheets')

    # Create spool sheet for sample data
    create_spool_sheet(sample_pipes, 'Spool_001')

    print('Spool creation complete. Check spool_sheets directory for outputs.')