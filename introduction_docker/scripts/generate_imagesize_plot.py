from __future__ import annotations


import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401

plt.rcParams['legend.title_fontsize'] = 'x-large'
plt.figure(figsize=(3.5, 2.625))


def main() -> int:

    x = ["ubuntu:latest", "debian:latest", "alpine:latest"]
    y = [117, 77.8, 7.33]
    bar_colors = ['#FF2C00', '#FF9500', '#00B945', '#845B97', '#474747', '#9e9e9e']

    with plt.style.context('science'):
        fig, ax = plt.subplots(figsize=(3.5, 2.625))
        ax.bar(x, y, label=x, color=bar_colors)

        ax.set_ylabel('Size (mb)')
        ax.set_title('Size of different images')
        ax.legend(title='Images')

        ax.bar_label(ax.containers[0])

        ax.legend(title="Imagesize", fontsize=12, bbox_to_anchor=(1, 1.05))
        ax.set_ylim((0, 130))
        # ax.set(xlabel=r'Distance (cm)')
        # ax.set(ylabel=r'Spannungsverteilung (\%)')
        print(f"Figuresize: {fig.get_size_inches()}")
        fig.savefig(f'image_sizes.eps', format='eps')

    x = ["Dockerfile 1", "Dockerfile 2"]
    y = [84, 84]
    bar_colors = ['#FF2C00', '#FF9500', '#00B945', '#845B97', '#474747', '#9e9e9e']

    with plt.style.context('science'):
        fig, ax = plt.subplots(figsize=(3.5, 2.625))
        ax.bar(x, y, label=x, color=bar_colors)

        ax.set_ylabel('Size (mb)')
        ax.set_title('Size of Dockerfile 1 and Dockerfile 2')
        ax.legend(title='Images')

        ax.bar_label(ax.containers[0])

        ax.legend(title="Imagesize", fontsize=12, bbox_to_anchor=(1, 1.05))
        ax.set_ylim((0, 100))
        # ax.set(xlabel=r'Distance (cm)')
        # ax.set(ylabel=r'Spannungsverteilung (\%)')
        print(f"Figuresize: {fig.get_size_inches()}")
        fig.savefig(f'dockerfile_cmdorder.eps', format='eps')

    return 0


if __name__ == "__main__":
    raise SystemExit(main())