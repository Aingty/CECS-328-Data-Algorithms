clc     %clear the command window
clear   %remove the items in workspace
% % doc for %doc = Reference page in Help browser
%% Arrays
x=[1 4 6 8 9 3];
x(2)
a = [1 4 5 7 9 0 2 3];
a(end) % prints the last element in the array
a(end) = []; % Delete the last element 
a
length(a)
size(a)
size(a,1)
size(a,2)
% z = zeros(2);
% z = zeros(2,1); 
% one = ones(2,1);
% % % 
%% For loops
for j=1:length(x) %for loop (for more info look at the help)
    y(j)=x(j);
end
% % % 
% % % %%************
%% If condition
a=6;
b=7;
if a==b
    0
elseif a>=b
    1
elseif a~=b & a>b
    2
else
    3
end
%% Functions
[minn, maxx, ave] = mnmxave(8 , 10);
 hello %hello world function
% % %%%*******     
%% Reading inputs
% % %Creates and opens input dialog box
answer = inputdlg('Please enter a number:','Pouye says')
str2num(answer{1})
result = input('Please enter a number: ') %requests user input a number/array/matrix
result2 = input('What is your name? ','s') %returns the entered text as a string
% % % %%************
%% Sorting..
sortedX = sort(x);
% % % % %%************
%% Timer
sum=0;
tic %Start stopwatch timer
for j=1:(length(x))^3 %for loop (for more info look at the help)
    sum=sum+1; 
end
% toc %Read elapsed time from stopwatch
t=toc
%%