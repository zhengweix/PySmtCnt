import React, { useState, useEffect } from "react";
import { AccountForm } from "./components";
import "./App.css";

function App() {
    const [accounts, setAccounts] =  useState([]);
    const [isFetching, setIsFetching] =  useState(false);
    useEffect(() => {
        fetch("/api/accounts")
            .then(response => response.json().then(setAccounts))
            .catch(alert)
            .finally(() => {
                setIsFetching(false);
            })
    }, []);
    return (
        <>
            <div className="App">
                <AccountForm accounts={accounts} />
            </div>
        </>
    );
}

export default App;