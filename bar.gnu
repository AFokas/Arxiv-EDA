set term pngcairo size 3500,1000
set rmargin screen 0.9
set key off
set output "bar.png"
set boxwidth 0.1
set offset 0.1
set xtic rotate by -45 offset -0.1 
set style fill solid
set ytic 10
set border linewidth 2
set ylabel 'Average Number of Collaborators'  font ",20"
set xlabel font ",30"
set xtic nomirror
set title 'Average Number of Collaborators in each Subcategory' font ",30"
plot "collab_subect_df.txt" using 2:xtic(1) w boxes

