%test histeq
I = imread('gray.jpg');
[J] = Histogram_equalization(I);
figure, imshow(I)
figure, imshow(J)
