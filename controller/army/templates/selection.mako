<%inherit file='base.mako' />

% if existing:
<div style="border: 1px solid">
    <form method="GET" action="/army/edition">
        <p>Choose your army below :</p>
        <select name="chosen_army">
            % for army in choices:
            <% 
                id = army['id'] 
                name = army['name']
            %>
            <option value=${id}>${name}</option>
            % endfor
        </select>
        <input type="submit" name="Ok" />
    </form>
</div>
%endif

<div style="border: 1px solid">
    <form method="POST" action="/army/new">
        <p>Or type a name for your new army:</p>
        <input type="text" name="army_name" />
        <input type="submit" name="Ok" />
    </form>
</div
