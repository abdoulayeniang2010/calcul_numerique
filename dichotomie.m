%methode de dichotomie 

%tracer du graphe 
d=0.1;
x=0:d:8;
f=@(x) x.^3-9*x.^2+18*x-6;
plot(x,f(x),'r','linewidth',3)
xlabel('axe des abcisses');
ylabel('axe des ordonnees');
grid on


a=0;
b=1;
iteration=0;
m=0; %valeur de la racine 
epsilon = 0.001; % la tolerance 
while(abs(b-a)>=epsilon)
    m=(a+b)/2;
    if f(a)*f(m)<0
        b=m;
    else
        a=m;
    end
    iteration=iteration+1;
end
disp(m);
disp(iteration);

