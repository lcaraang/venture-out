function main() {
    d3.json("/jsondata").then(function (data) {
        d3.selectAll("text")
            .data(data, function (d) { return this.id || d.location; })
            .text(d => d.location + " (" + d.count + ")");

        var total =
            d3.rollups(
                data,
                counts => d3.sum(counts, d => d.count),
            )

        d3.selectAll("g").append("text")
            .attr("x", 50)
            .attr("y", 75)
            .text("Total Posts: " + total);
    })
}
