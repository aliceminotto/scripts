redm=importdata('mMet/2/mMet_copiA.out');
red35=importdata('35min/2/35min_copiA.out');
greenm=importdata('mMet/3/mMet_copiA.out');
green35=importdata('35min/3/35min_copiA.out');

figure(1);
plot(greenm(:,1),greenm(:,2:end),'-g');
hold on;
plot(redm(:,1),redm(:,2:end),'r-');
xlabel('time');
ylabel('fluorescence');
title('mMet');
hold off;

figure(2);
plot(green35(:,1),green35(:,2:end),'-g');
hold on;
plot(red35(:,1),red35(:,2:end),'r-');
xlabel('time');
ylabel('fluorescence');
title('mMet 35min');
hold off;

figure(3);
time=greenm(:,1)
for i = 1:size(time)
    averagegm(i)=nanmean(greenm(i,2:end));
    averagerm(i)=nanmean(redm(i,2:end));
    averageg35(i)=nanmean(green35(i,2:end));
    averager35(i)=nanmean(red35(i,2:end));
end;
plot(time,averagegm(:),'-g');
hold on;
plot(time,averagerm(:),'r-');
xlabel('time');
ylabel('fluorescence');
title('average mMet');
hold off;
figure(4);
plot(time,averageg35(:),'-g');
hold on;
plot(time,averager35(:),'r-');
xlabel('time');
ylabel('fluorescence');
title('average mMet 35min');
hold off;

greenmfit=importdata('mMet/3/mMet_fittato.out');
green35fit=importdata('35min/3/35min_fittato.out');
redmfit=importdata('mMet/2/mMet_fittato.out');
red35fit=importdata('35min/2/35min_fittato.out');

figure(5);
scatter(redmfit(:,2),greenmfit(:,2));
coeffm=corr(redmfit(:,2),greenmfit(:,2))
xlabel('red channel');
ylabel('green channel');
title('mMet');

figure(6);
scatter(red35fit(:,2),green35fit(:,2));
coeff35=corr(red35fit(:,2),green35fit(:,2))
xlabel('red channel');
ylabel('green channel');
title('mMet 35 min');

figure(7);
rescaled_redmfit=redmfit(:,2)/mean(redmfit(:,2));
ksdensity(rescaled_redmfit);
stdredm=std(rescaled_redmfit)
%cvredm=stdredm/mean(redmfit(:,2))
hold on;
rescaled_greenmfit=greenmfit(:,2)/mean(greenmfit(:,2));
ksdensity(rescaled_greenmfit);
stdgreenm=std(rescaled_greenmfit)
%cvgreenm=stdgreenm/mean(greenmfit(:,2))
title('mMet distribution');
covarm=sqrt(var(rescaled_redmfit+rescaled_greenmfit)/(2*mean(rescaled_redmfit)*mean(rescaled_greenmfit)))
intnm=sqrt(mean((rescaled_redmfit-rescaled_greenmfit).^2)/2)
extnm=sqrt(mean(rescaled_redmfit.*rescaled_greenmfit)-1)

[f,p]=kstest2(rescaled_redmfit,rescaled_greenmfit)

figure(8);
rescaled_red35fit=red35fit(:,2)/mean(red35fit(:,2));
ksdensity(rescaled_red35fit);
stdred35=std(rescaled_red35fit)
%cvred35=stdred35/mean(red35fit(:,2))
hold on;
rescaled_green35fit=green35fit(:,2)/mean(green35fit(:,2));
ksdensity(rescaled_green35fit);
stdgreen35=std(rescaled_green35fit);
%cvgreen35=stdgreen35/mean(green35fit(:,2))
title('mMet 35 min distribution')
covar35=sqrt(var(rescaled_red35fit+rescaled_green35fit)/(2*mean(rescaled_red35fit)*mean(rescaled_green35fit)))
intn35=sqrt(mean((rescaled_red35fit-rescaled_green35fit).^2)/2)
extn35=sqrt(mean(rescaled_red35fit.*rescaled_green35fit)-1)

[f1,p1]=kstest2(rescaled_red35fit,rescaled_green35fit)

%figure(9);
