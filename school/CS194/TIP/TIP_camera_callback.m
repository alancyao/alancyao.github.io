function [  ] = TIP_camera_callback( ~, data )
% Janky callback function for navigating 3d scenes.
% NOTE: This assumes that the camera up vector is [0 1 0],
% and contrary to canonical camera coordinates, assumes that
% the camera is looking down the +z axis.
%
% Called as follows:
% figure('KeyPressFcn', @TIP_camera_callback); hold on;
% <Render all your planes etc here>
% axis equal; axis vis3d; axis off;  
% camproj('perspective');

pos = campos; lookat = camtarget;
div = 100;
w = 1000; d = 1000; h = 1000; %box dimensions

switch data.Key
    case double('s') %strafe down
        pos(2) = pos(2) - w/div;
    case double('w') %strafe up
        pos(2) = pos(2) + w/div;
    case double('d') %strafe right
        pos(1) = pos(1) + h/div;
    case double('a') %strafe left
        pos(1) = pos(1) - h/div;
    case double('e') %move forward
        pos(3) = pos(3) + d/div;
    case double('q') %move backward
        pos(3) = pos(3) - d/div;
    case 'leftarrow' %rotate left
        lookat(1) = lookat(1) - w/div;
    case 'uparrow' %up
        lookat(2) = lookat(2) + h/div;
    case 'rightarrow' %right
        lookat(1) = lookat(1) + w/div;
    case 'downarrow' %down
        lookat(2) = lookat(2) - h/div;
end
campos(pos); camtarget(lookat);
end

