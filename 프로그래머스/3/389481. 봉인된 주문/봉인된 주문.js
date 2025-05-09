function solution(n, bans) {
    // 주문 길이별 누적 문자열 개수 구하기
    const lengths_sum = Array(12).fill(0);
    for (let l = 1; l <= 11; l++) {
        lengths_sum[l] = lengths_sum[l - 1] + Math.pow(26, l);
    }

    // 문자열 s의 사전 순위(rank)를 구하는 함수
    function rank(s) {
        const length = s.length;
        let res = lengths_sum[length - 1];

        for (let i = 0; i < length; i++) {
            const ch = s.charCodeAt(i) - 'a'.charCodeAt(0); // 몇 번째 알파벳인지 알아내기
            res += ch * Math.pow(26, length - i - 1);
        }
        return res + 1;
    }

    // 사전 순위 k번째 문자열을 구하는 함수
    function kth_string(k) {
        for (let length = 1; length <= 11; length++) {
            const cnt = Math.pow(26, length);
            if (k <= cnt) {
                const res = [];
                k--;

                for (let i = 0; i < length; i++) {
                    const div = Math.pow(26, length - i - 1);
                    const ch_idx = Math.floor(k / div);
                    res.push(String.fromCharCode('a'.charCodeAt(0) + ch_idx));
                    k %= div;
                }
                return res.join('');
            }
            k -= cnt;
        }
    }

    // bans를 rank로 변환 + 정렬
    const bans_ranked = bans.map(rank).sort((a, b) => a - b);

    // rank <= k인 bans의 개수를 구하는 함수
    function count_bans_upto(bans_ranked, k) {
        let left = 0, right = bans_ranked.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (bans_ranked[mid] <= k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    // 이분 탐색으로 정답 rank 찾기
    const total = lengths_sum[11];  // 전체 문자열 개수
    let left = 1, right = total;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const removed = count_bans_upto(bans_ranked, mid);
        const actual = mid - removed;

        if (actual < n) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return kth_string(left);
}