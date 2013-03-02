<%inherit file='base.mako' />


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
        <b>Instant effect(s)</b>
        <ul>
        % for instant_name, instant_description in instants:
            <button type="button" disabled="true">${instant_name}</button>
            <li>${instant_description}</li>
        % endfor
        </ul>
        <hr />
        <b>Special effect(s)</b>
        <ul>
        % for special_name, special_description in specials:
            <button type="button" disabled="true">${special_name}</button>
            <li>${special_description}</li>
        % endfor
        </ul>
        <hr />
        <b>Result</b>
        <ul>
        % for result_type, sum in sums:
            <li>${result_type}: ${sum}</li>
        % endfor
        </ul>
    </div>
    <form method="get" action="/army/selection">
        <input type="submit" value="Return to selection" />
    </form>
    <form method="get" action="/army/${army_id}/edition">
        <input type="submit" value="Edit the army" />
    </form>
    <form method="get" action="/army/${army_id}/roll/dragon" style="display: inline-block;">
        <input type="submit" value="Dragon Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/melee" style="display: inline-block;">
        <input type="submit" value="Melee Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/missile" style="display: inline-block;">
        <input type="submit" value="Missile Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/maneuver" style="display: inline-block;">
        <input type="submit" value="Maneuver Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/melee_save" style="display: inline-block;">
        <input type="submit" value="Melee Save Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/missile_save" style="display: inline-block;">
        <input type="submit" value="Missile Save Roll" />
    </form>
</div>
