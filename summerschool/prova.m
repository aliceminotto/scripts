singlem=importdata('oldexpt/single/single_copiA.out');
multiplem=importdata('oldexpt/multiple/multiple_copiA.out');
time=singlem(:,1);
figure(1),
plot(time,singlem(:,2:end),'-b');
hold on,
plot(time,multiplem(:,2:end),'-r');
xlabel('time');
ylabel('fluorescence');
hold off;

%figure(2),
%plot(time,singlem(:,nanmean(2:end)),'-b');
%hold on,
%plot(time,multiplem(:,nanmean(2:end)),'-r');

figure(2);
for i = 1:size(time)
    average(i)=nanmean(singlem(i,2:end));
    average2(i)=nanmean(multiplem(i,2:end));
end;
plot(time,average(:),'-b');
hold on;
plot(time,average2(:),'-r');
xlabel('time');
ylabel('average fluorescence');
hold off;

slopes=(average(24)-average(11))/13
slopem=(average2(24)-average2(6))/18

singlefit=importdata('oldexpt/single/single_fittato.out');
multfit=importdata('oldexpt/multiple/multiple_fittato.out');
figure(3);
ksdensity(singlefit(:,2));
meansingle=mean(singlefit(:,2))
stdsingle=std(singlefit(:,2))
cvsingle=stdsingle/meansingle
hold on;
ksdensity(multfit(:,2));
meanmult=mean(multfit(:,2))
stdmult=std(multfit(:,2))
cvmult=stdmult/meanmult

meanmult/meansingle