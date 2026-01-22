"""Plotly Sankey diagram helpers for quick experimentation."""

from __future__ import annotations

import json
import urllib.request
from typing import Sequence

import plotly.graph_objects as go

ENERGY_SANKEY_URL = (
    "https://raw.githubusercontent.com/plotly/plotly.js/master/"
    "test/image/mocks/sankey_energy.json"
)


def load_energy_sankey_data(url: str = ENERGY_SANKEY_URL) -> dict:
    """Load the Plotly energy Sankey mock JSON.

    Note: this performs a network request.
    """

    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def basic_sankey() -> go.Figure:
    labels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    source = [0, 1, 0, 2, 3, 3]
    target = [2, 3, 3, 4, 4, 5]
    value = [8, 4, 2, 8, 4, 2]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    color="blue",
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )
    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    return fig


def colored_links_sankey(data: dict | None = None, opacity: float = 0.4) -> go.Figure:
    """Sankey diagram with link colors derived from their source node."""

    if data is None:
        data = load_energy_sankey_data()

    node_colors = [
        "rgba(255,0,255, 0.8)" if color == "magenta" else color
        for color in data["data"][0]["node"]["color"]
    ]
    link_colors = [
        node_colors[src].replace("0.8", str(opacity))
        for src in data["data"][0]["link"]["source"]
    ]

    fig = go.Figure(
        data=[
            go.Sankey(
                valueformat=".0f",
                valuesuffix="TWh",
                node=dict(
                    pad=15,
                    thickness=15,
                    line=dict(color="black", width=0.5),
                    label=data["data"][0]["node"]["label"],
                    color=node_colors,
                ),
                link=dict(
                    source=data["data"][0]["link"]["source"],
                    target=data["data"][0]["link"]["target"],
                    value=data["data"][0]["link"]["value"],
                    label=data["data"][0]["link"]["label"],
                    color=link_colors,
                ),
            )
        ]
    )
    fig.update_layout(title_text="Energy forecast for 2050", font_size=10)
    return fig


def styled_sankey(data: dict | None = None) -> go.Figure:
    """Sankey diagram with a dark background and hovermode styling."""

    if data is None:
        data = load_energy_sankey_data()

    fig = go.Figure(
        data=[
            go.Sankey(
                valueformat=".0f",
                valuesuffix="TWh",
                node=dict(
                    pad=15,
                    thickness=15,
                    line=dict(color="black", width=0.5),
                    label=data["data"][0]["node"]["label"],
                    color=data["data"][0]["node"]["color"],
                ),
                link=dict(
                    source=data["data"][0]["link"]["source"],
                    target=data["data"][0]["link"]["target"],
                    value=data["data"][0]["link"]["value"],
                    label=data["data"][0]["link"]["label"],
                ),
            )
        ]
    )

    fig.update_layout(
        hovermode="x",
        title=dict(text="Energy forecast for 2050"),
        font=dict(size=10, color="white"),
        plot_bgcolor="black",
        paper_bgcolor="black",
    )
    return fig


def link_hovercolor_sankey() -> go.Figure:
    labels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    source = [0, 1, 0, 2, 3, 3]
    target = [2, 3, 3, 4, 4, 5]
    value = [8, 4, 2, 8, 4, 2]
    hovercolor = [
        "midnightblue",
        "lightskyblue",
        "gold",
        "mediumturquoise",
        "lightgreen",
        "cyan",
    ]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    color="blue",
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value,
                    hovercolor=hovercolor,
                ),
            )
        ]
    )
    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    return fig


def hovertemplate_sankey() -> go.Figure:
    labels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    source = [0, 1, 0, 2, 3, 3]
    target = [2, 3, 3, 4, 4, 5]
    value = [8, 4, 2, 8, 4, 2]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    customdata=[
                        "Long name A1",
                        "Long name A2",
                        "Long name B1",
                        "Long name B2",
                        "Long name C1",
                        "Long name C2",
                    ],
                    hovertemplate=(
                        "Node %{customdata} has total value %{value}"
                        "<extra></extra>"
                    ),
                    color="blue",
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value,
                    customdata=["q", "r", "s", "t", "u", "v"],
                    hovertemplate=(
                        "Link from node %{source.customdata}<br />"
                        "to node%{target.customdata}<br />"
                        "has value %{value}<br />"
                        "and data %{customdata}<extra></extra>"
                    ),
                ),
            )
        ]
    )
    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    return fig


def positioned_sankey() -> go.Figure:
    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                label=["A", "B", "C", "D", "E", "F"],
                x=[0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
                y=[0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
                pad=10,
            ),
            link=dict(
                source=[0, 0, 1, 2, 5, 4, 3, 5],
                target=[5, 3, 4, 3, 0, 2, 2, 3],
                value=[1, 2, 1, 1, 1, 1, 1, 2],
            ),
        )
    )
    return fig


def arrow_links_sankey() -> go.Figure:
    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                label=["A", "B", "C", "D", "E", "F"],
                x=[0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
                y=[0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
                pad=10,
                align="right",
            ),
            link=dict(
                arrowlen=15,
                source=[0, 0, 1, 2, 5, 4, 3, 5],
                target=[5, 3, 4, 3, 0, 2, 2, 3],
                value=[1, 2, 1, 1, 1, 1, 1, 2],
            ),
        )
    )
    return fig


def alignment_sankey(align: str = "left") -> go.Figure:
    """align options: left, right, center, justify"""

    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                label=["0", "1", "2", "3", "4", "5"],
                align=align,
            ),
            link=dict(
                arrowlen=15,
                source=[0, 1, 4, 2, 1],
                target=[1, 4, 5, 4, 3],
                value=[4, 2, 3, 1, 2],
            ),
        )
    )
    return fig


def concept_prediction_sankey(
    concepts: Sequence[str],
    predictions: Sequence[str],
    flows: Sequence[Sequence[float]],
    concept_colors: Sequence[str] | None = None,
    prediction_color: str = "#111827",
) -> go.Figure:
    """Create a left-to-right Sankey from concepts to predictions.

    flows is a matrix with shape (len(concepts), len(predictions)).
    """

    if len(flows) != len(concepts):
        raise ValueError("flows rows must match number of concepts")

    labels = list(concepts) + list(predictions)
    source: list[int] = []
    target: list[int] = []
    value: list[float] = []

    for i, row in enumerate(flows):
        if len(row) != len(predictions):
            raise ValueError("each flow row must match number of predictions")
        for j, v in enumerate(row):
            if v == 0:
                continue
            source.append(i)
            target.append(len(concepts) + j)
            value.append(float(v))

    if concept_colors is None:
        concept_colors = go.Figure().layout.template.layout.colorway or []

    if not concept_colors:
        concept_colors = ["#4c78a8", "#72b7b2", "#f58518", "#e45756", "#54a24b"]

    concept_colors = list(concept_colors)
    concept_color_list = [
        concept_colors[i % len(concept_colors)] for i in range(len(concepts))
    ]
    node_colors = concept_color_list + [prediction_color] * len(predictions)
    link_colors = [concept_color_list[src] for src in source]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=18,
                    thickness=18,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    color=node_colors,
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )
    fig.update_layout(
        title_text="Concept -> Predictions",
        font_size=11,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="black"),
    )
    fig.data[0].link.color = link_colors
    return fig
