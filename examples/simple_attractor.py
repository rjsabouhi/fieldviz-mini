from fieldviz_mini import spiral_sink, plot_vector_field, plot_streamlines

field = spiral_sink()
plot_vector_field(field)
plot_streamlines(field, seeds=[(1,1), (-1,0), (0.5,-1)])
