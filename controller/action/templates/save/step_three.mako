<%inherit file='controller:templates/base.mako' />

<table style="border: 1px solid black; display: inline-block; width: 40%;">
    % for dice_name, face_list, desc_list in results:
        <tr style="border: 1px solid black; width: 100px;">
            <td>${dice_name}</td>
            <td  style="width: 150px;">
        % for picture in face_list:
                <img class="picture" src="http://www.sfr-inc.com/${picture}" />
        % endfor
            </td>
        <% desc = ' ; '.join(desc_list) %>
            <td style="width: 250px;">${desc}</td>
        </tr>
    % endfor
    <tr style="border: 1px solid black; width: 100px;">
        <td colspan="3">Results : ${save} for ${damage}, ${remaining} casualties</td>
    </tr>
</table>
<div style="border: 1px solid; display: inline-block; vertical-align: top; width: 40%;">

    <b>The survivor</b>
    % for name, picture in dices:
    <div class="block">
        <div class="name">${name}</div>
        <img class="picture" src="http://www.sfr-inc.com/${picture}" />
    </div>
    % endfor
    <hr />
    <b>The fallen</b>
    % for name, picture in dead_dices:
    <div class="fallen block">
        <div class="name">${name}</div>
        <img class="picture" src="http://www.sfr-inc.com/${picture}" />
    </div>
    % endfor
    <form method="get" action="${route_next_step}">
        <input type="submit" value="Return to army selection" />
    </form>
</div>
