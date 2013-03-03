<div style="width: 70%; margin-left: 15%; margin-right: 15%;">
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
    </table>
    <div style="border: 1px solid; display: inline-block; vertical-align: top; width: 40%;">

        <b>Remaining army</b>
        % for name, picture in dices:
        <div class="block">
            <div class="name">${name}</div>
            <img class="picture" src="http://www.sfr-inc.com/${picture}" />
        </div>
        % endfor
    <form method="get" action="${route_next_step}">
        <input type="submit" value="Return to army selection" />
    </form>
    </div>
</div>
