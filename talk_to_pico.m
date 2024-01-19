bridge1 = serialport('COM5',9600);
% connect to the pi pico to set current, the name of the serialport can be
% looked up in device manager. In my case it is 'COM5'.

msg = join(['I ',num2str(0.088)]);
% the message sent to the pi pico, which set the current to 0.088 A

write(bridge1,msg,"string");
% set current