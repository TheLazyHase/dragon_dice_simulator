<%inherit file='base.mako' />

% if existing:
<div style="border: 1px solid">
    <form method="POST" action="/army/">
        <p>Choose your army below :</p>
        <select name="chosen_army">
            ${ choices | n }
        </select>
    </form>
</div>
%endif

<div style="border: 1px solid">
    <form method="POST" action="/army/new">
        <p>Type a name for your new army:</p>
        <input type="text" name="army_name" />
        <input type="submit" name="Ok" />
    </form>
</div
