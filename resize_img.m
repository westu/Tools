input_path = '';
output_path = '';
fs = dir(input_path);
for i = 3 : 1 : size(fs, 1)
    im = imread(strcat(input_path, filesep, fs(i).name));
    im = imresize(im, [100, 100], 'bicubic');
    imwrite(im, strcat(output_path, filesep, fs(i).name));
end
