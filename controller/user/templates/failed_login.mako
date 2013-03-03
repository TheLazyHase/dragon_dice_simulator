<div style="width: 70%; margin-left: 15%; margin-right: 15%;">
    Failed login !    
    <form method="POST" action="${authentication_route}">
        <p>Choose your login :</p>
        <select name="id">
            % for id in user_ids:
            <option value=${id}>Player #${id}</option>
            % endfor
        </select>
        <input type="submit" value="Ok" />
    </form>
</div>
