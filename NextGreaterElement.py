vector<long long> nextLargerElement(vector<long long> a, int n){
        // Your code here
        stack<long long int>s;
        vector<long long int>v(n,-1);
        long long int i=n-1;
        s.push(a[i]);
        long long int j=2;
        i--;
        while (i>=0){
            if (s.top()<a[i]){
                //cout<<s.top()<<s.size()<<" ";
                s.pop();
                if (s.size()==0){
                    s.push(a[i]);
                    i--;
                    j++;
                }
            }
            else{
                v[n-j]=s.top();
                s.push(a[i]);
                j++;
                i--;
            }
        }/*
        cout<<"\n";
        for (auto it:v)
            cout<<it<<" ";
        cout<<"\n";*/
        return v;
