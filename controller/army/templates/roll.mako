<%inherit file='base.mako' />


<div style="border: 1px solid">
    Roll:
    % for result in results:
        <div>${result}</div>
    % endfor
</div>
<div style="border: 1px solid">
    Effects:
    % for event in events:
        <div>${event}</div>
    % endfor
</div>
<div style="border: 1px solid">
    Result:
    % for result_type, sum in sums:
    ${result_type}: ${sum}<br />
    % endfor
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
