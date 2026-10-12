import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    length = len(sys.argv)
    if length < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = list()
        for arg in sys.argv[1:]:
            try:
                num = int(arg)
                scores.append(num)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(scores) == 0:
            print("No scores provided. "
                  "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            print(rf"""
                \_\     /_/        \/_/         /_/      \/_/   \_\     /_/
                .-.  \.-./  .-.   .-./  .-.   .-./  .-.   .-\   .-.  \.-./  .-.
            //-\\_//-\\_//-\\_//-\\_//-\\_//-\\_// \\_//-\\_//-\\_//-\\_//-\\
            __(   '-'   '-'\  '-'   '-'  /'-'   '-'\__'-'   '-'__/'-'   '-'\__
            /_/))            \__       __/\          \_\       /_/           \_
        ___\_//
        /_/  ((        Scores processed: {scores}
            )) __
        __   // /_/     Total players: {len(scores)}
        \_\_((_/___
            ))  \_     Total score: {sum(scores)}
            \\
            )) _        Average score: {sum(scores) / len(scores)}
        __   // /_/
        \_\_((         High score: {max(scores)}
            \\
            )) _        Low score: {min(scores)}
        __   // /_/
        \_\_((_/___    Score range: {max(scores) - min(scores)}
            ))  \_\                __                    __
            \\     __       __     \_\  __          __   \_\  __   __       __
        __  ))    \_\     /_/        \/_/         /_/      \/_/   \_\     /_/
        \_\_((   .-.  \.-./  .-.   .-./  .-.   .-./  .-.   .-\   .-.  \.-./  .-
            \\_//-\\_//-\\_//-\\_//-\\_//-\\_//-\\_// \\_//-\\_//-\\_//-\\_//-\
                'dc\__'-'   '-'\  '-'   '-'  /'-'   '-'\__'-'   '-'__/'-'   '-'
            """)


if __name__ == "__main__":
    main()
